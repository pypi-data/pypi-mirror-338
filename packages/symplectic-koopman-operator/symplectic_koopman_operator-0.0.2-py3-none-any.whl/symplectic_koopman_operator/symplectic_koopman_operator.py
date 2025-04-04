import typing
import warnings
from collections import OrderedDict
import torch
import torch.nn as nn
import torch.nn.functional as F
import SympNetsTorch as snn
from .functional import pure_rotation


class frequency_network(nn.Module):
    def __init__(
        self, linear_tune: float, dim: int = 1, alpha: float = 1, hidden_size: int = 100
    ) -> None:
        """A class to predict the frequency of dim pure N-D rotation(s)."""
        super().__init__()
        self.dim = dim  # Spacial dimension
        self.alpha = alpha  # Alpha hyperparameter for the tune function
        self.linear_tune = linear_tune  # The linear tune of the map
        self.is_frozen = False  # Whether the network is frozen or not

        input_size = 2 * self.dim
        self.layers = nn.ModuleList(
            [
                nn.Linear(input_size, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, self.dim),
            ]
        )

    def tune(self, x: torch.Tensor) -> torch.Tensor:
        """Takes in batched data and returns the tune of the data."""
        r = x[..., : 2 * self.dim].clone()  # ignore sign

        if x.shape[1] > 2 * self.dim:
            sign = x[..., -1].clone()

        else:
            # default to forward time
            sign = torch.ones(x.shape[0], dtype=torch.int32).to(x.device)

        if not self.is_frozen:
            for layer in self.layers:
                r = layer(r)

            # dQ between -1 and 1
            dtune = 1 - 2 / (1 + torch.exp(self.alpha * r))

        else:
            dtune = torch.tensor(0.0, dtype=x.dtype).to(x.device)

        _tune = self.linear_tune + dtune

        return sign.unsqueeze(-1) * _tune  # unsqueeze for correct broadcasting

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.tune(x)

    def freeze(self, state: bool) -> None:
        # If the model is frozen, the gradients are not calculated
        self.is_frozen = state

        for param in self.parameters():
            param.requires_grad_(requires_grad=not state)


class koopman_operator(nn.Module):
    """
    A PyTorch module representing a Koopman operator.

    This class implements a Koopman operator, which is a linear transformation used in
    the analysis of dynamical systems. The operator is implemented as a neural network
    with a frequency network and several layers including dropout, activation, and
    linear layers.

    Parameters
    ----------
    dim : int
        The spatial dimension of the input data. Currently hardcoded to 1.
    frequency_model_state_dict :
        The frequency network used in the forward pass of the operator.
    ncoder : int, optional
        The number of matrices in the linear encoder modules. Maximum is 9.
        Default is 9.
    nactivation : int, optional
        The number of activation modules. Default is 3.
    dropout_probability : float, optional
        The dropout probability for the dropout layer. Default is 0.25.

    Attributes
    ----------
    dim : int
        The spatial dimension of the input data. Currently hardcoded to 1.
    ncoder : int
        The number of matrices in the linear encoder modules. Maximum is 9.
    frequency_model : frequency_network
        The frequency network used in the forward pass of the operator.
    dropout_layer : nn.Dropout
        A dropout layer used in the operator.
    encoder_layers : nn.ModuleList
        A list of layers used in the operator, including linear, dropout, and
        activation layers.

    Methods
    -------
    transform(x)
        Applies the operator to the input tensor x.
    inverse(x)
        Applies the inverse of the operator to the input tensor x.
    tune(x)
        Applies the frequency model to the input tensor x.
    forward(x)
        Applies the forward pass of the operator to the input tensor x, which includes
        applying the frequency network, the operator, a pure rotation, and the inverse
        operator.

    Properties
    ----------
    is_frozen : bool
        Whether the frequency model is frozen or not.
    """

    def __init__(
        self,
        dim: int,
        ncoder: int,
        nactivation: int = 3,
        frequency_model_state_dict: typing.OrderedDict | frequency_network = None,
        linear_tune: float = None,  # Only used if frequency_model_state_dict is None
        frequency_alpha: float = 1.0,
    ):
        super().__init__()

        self.dim = dim  # Spacial dim
        self.ncoder = ncoder  # Number of matrixes in Linear encoder modules
        self.nactivation = nactivation  # Number of activation modules
        self.linear_tune = linear_tune

        if self.ncoder > 9:
            warnings.warn(
                "More than 9 matrices in the encoder module. This should be unnecessary."
            )

        if isinstance(frequency_model_state_dict, frequency_network):
            # This means the model is part of a large koopman operator model and should
            # use the same frequency network as all the other layers
            self.frequency_model = frequency_model_state_dict

        elif isinstance(frequency_model_state_dict, OrderedDict):
            self.frequency_model = frequency_network(
                linear_tune=self.linear_tune, dim=self.dim, alpha=frequency_alpha
            )
            self.frequency_model.load_state_dict(frequency_model_state_dict)

        elif frequency_model_state_dict is None:
            self.frequency_model = frequency_network(
                linear_tune=self.linear_tune, dim=self.dim, alpha=frequency_alpha
            )

        else:
            raise ValueError(
                "frequency_model_state_dict must be an OrderedDict, frequency_network, or None, got {}".format(
                    type(frequency_model_state_dict)
                )
            )

        # Generating encoder layers

        # ! Dropout layers are not used in the final model, they interfere with the
        # ! tune variance loss. They will give zero output => undefined angles.

        layers = []
        up_or_low_Activation = iter(("up", "low", "low", "up"))
        up_or_low_Linear = iter(("low", "up", "up", "low"))
        layers = [
            snn.Linear(dim=self.dim, up_or_low=next(up_or_low_Linear), n=self.ncoder)
        ]

        for _ in range(self.nactivation):
            layers.append(
                snn.Activation(
                    func=F.tanh, dim=self.dim, up_or_low=next(up_or_low_Activation)
                )
            )
            layers.append(
                snn.Linear(
                    dim=self.dim, up_or_low=next(up_or_low_Linear), n=self.ncoder
                )
            )

        # Good layers
        # layers = [
        #     snn.Linear(dim=self.dim, up_or_low="low", n=self.ncoder),
        #     snn.Activation(func=F.tanh, dim=self.dim, up_or_low="up"),
        #     snn.Linear(dim=self.dim, up_or_low="up", n=self.ncoder),
        #     snn.Activation(func=F.tanh, dim=self.dim, up_or_low="low"),
        #     snn.Linear(dim=self.dim, up_or_low="up", n=self.ncoder),
        #     snn.Activation(func=F.tanh, dim=self.dim, up_or_low="low"),
        #     snn.Linear(dim=self.dim, up_or_low="low", n=self.ncoder),
        # ]

        self.encoder_layers = nn.ModuleList(layers)

    def transform(self, x: torch.Tensor) -> torch.Tensor:
        """Takes in batched data and applies the Koopman operator to it."""
        xp = x[..., : 2 * self.dim].clone()  # ignore sign

        for layer in self.encoder_layers:
            xp = layer(xp)

        return xp

    def inverse(self, x: torch.Tensor) -> torch.Tensor:
        """Takes in batched data and applies the inverse Koopman operator to it."""
        for layer in reversed(self.encoder_layers):
            if layer != self.dropout_layer:
                x = layer(x, inverse=True)

            else:
                x = layer(x)

        return x

    def tune(self, x: torch.Tensor) -> torch.Tensor:
        """Takes in batched data and applies the frequency model to it."""
        return self.frequency_model.tune(x)

    def forward(self, xp: torch.Tensor) -> typing.Tuple[torch.Tensor, torch.Tensor]:
        """Takes in windowed data and applies the Koopman operator and rotation to it."""
        data_shape = xp.shape

        x = xp.reshape(-1, 2 * self.dim)

        # Get tune and transformed data
        tune_ = self.tune(x)
        x = self.transform(x)

        # Store transformed data
        transformed_data = x.clone().reshape(data_shape)

        # Apply rotation, dropout, and inverse
        x = pure_rotation(x, tune_, counter_clockwise=False)
        x = self.inverse(x)

        # Store new data
        xp = x.clone().reshape(data_shape)

        return xp, transformed_data

    @property
    def is_frozen(self) -> bool:
        return self.frequency_model.is_frozen
