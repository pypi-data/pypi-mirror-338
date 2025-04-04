import typing
import torch
import torch.nn as nn
import torch.nn.functional as F


def transformed_tune_variance(transformed_data: torch.Tensor) -> torch.Tensor:
    """Calculates the angle variance loss for a given tensor.

    Parameters
    ----------
    X : torch.Tensor
        The input tensor for which the variance loss is to be calculated.

    Returns
    -------
    torch.Tensor
        The calculated variance loss.
    """

    # Get n+1 turn
    transformed_data1 = torch.roll(transformed_data, -1, dims=0)

    # Normalize the data
    # Ignore the last element, since we don't know if the last point will be one turn
    # behind the first point.
    d1 = transformed_data[:-1] / torch.linalg.norm(
        transformed_data[:-1], dim=-1, keepdim=True
    )
    d2 = transformed_data1[:-1] / torch.linalg.norm(
        transformed_data1[:-1], dim=-1, keepdim=True
    )

    # These checks take a lot of time, so we'll comment them
    # if torch.isnan(d1).any() or torch.isnan(d2).any():
    #     raise ValueError("NaN values in the data")

    # Calculate the cosine of the angle between the two vectors
    cth = torch.einsum("ij,ij->i", d1, d2)

    # These checks take a lot of time, so we'll comment them
    # if torch.isnan(cth).any():
    #     raise ValueError("NaN values in the data")

    # Shouldn't matter if we use cos or angles directly since it'll be normalized anyway
    loss = torch.var(cth)

    return loss


def transformed_amplitude_variance(transformed_data: torch.Tensor) -> torch.Tensor:
    """Calculates the amplitude variance loss for a given tensor.

    Parameters
    ----------
    X : torch.Tensor
        The input tensor for which the variance loss is to be calculated.

    Returns
    -------
    torch.Tensor
        The calculated variance loss.
    """

    loss = torch.var(torch.linalg.norm(transformed_data, dim=-1), dim=0)

    return loss


def exponential_loss(
    output: torch.Tensor,
    target: torch.Tensor,
    a: float = 1.0,
    p: float = 2.0,
    reduction: str = "mean",
) -> torch.Tensor:
    """
    Calculate the exponential loss between the predicted output and the target.

    This loss function computes the exponential of the scaled p-norm of the difference
    between the output and target tensors. It is designed to emphasize larger errors
    more significantly than smaller ones. The loss can be either summed up or averaged
    across all examples in the batch depending on the `reduction` parameter.

    Parameters
    ----------
    output : torch.Tensor
        The predicted outputs from the model. Shape is expected to be (N, *) where
        N is the batch size and * denotes any number of additional dimensions.
    target : torch.Tensor
        The ground truth values, expected to have the same shape as `output`.
    a : float, optional
        A scaling factor applied to the norm of the difference between `output` and
        `target`, by default 1.0.
    p : float, optional
        The order of the norm to be computed, by default 2.0. A `p` value of 2.0
        corresponds to the Euclidean distance.
    reduction : str, optional
        Specifies the reduction to apply to the output: 'mean' | 'sum'. 'mean'
        computes the mean loss per batch, while 'sum' computes the total loss
        across the batch, by default "mean".

    Returns
    -------
    torch.Tensor
        The calculated loss as a single-element tensor if `reduction` is 'sum',
        or a tensor of shape (N,) if `reduction` is 'mean', where N is the batch size.

    Raises
    ------
    ValueError
        If the `reduction` parameter is not 'mean' or 'sum'.

    Examples
    --------
    >>> output = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    >>> target = torch.tensor([[1.5, 2.5], [3.5, 4.5]])
    >>> loss = exponential_loss(output, target, a=1.0, p=2.0, reduction='mean')
    >>> print(loss)
    """

    if reduction not in ["mean", "sum"]:
        raise ValueError(f"Reduction method {reduction} not recognized.")

    loss = torch.sum(torch.exp(a * (output - target).norm(p=p, dim=-1)))

    if reduction == "mean":
        loss = loss / output.size()[0]

    return loss


def norm_parameter_loss(
    model: nn.Module,
    p: int,
    reduction: str = "mean",
    skip_model: typing.List[str] = None,
) -> torch.Tensor:
    """
    Calculate the norm of the parameters of a PyTorch model.

    This function computes the p-norm of each parameter of the given model and then
    reduces these norms according to the specified reduction method.

    Parameters
    ----------
    model : nn.Module
        The PyTorch model whose parameters' norm is to be calculated.
    p : int
        The order of the norm to be calculated. For example, p=2 calculates the 2-norm
        (Euclidean norm).
    reduction :  str, optional:
        The reduction method to apply to the norms. It can be either 'mean' or 'sum'.
        If 'mean', the function returns the mean of the norms.
        If 'sum', it returns the sum of the norms. Defaults to 'mean'.
    skip_model : list, optional:
        A list of strings containing the names of the modules whose parameters should
        be skipped when calculating the norm. Defaults to None.

    Returns
    -------
    loss: torch.Tensor
        The reduced norm of the parameters of the model.
    """
    if reduction not in ["mean", "sum"]:
        raise ValueError(f"Reduction method {reduction} not recognized.")

    loss = None
    num_params = 0

    if skip_model is None:
        skip_model = []

    for name, param in model.named_parameters():
        if any([name.startswith(skip) for skip in skip_model]):
            continue

        if loss is None:
            loss = param.norm(p=p)
        else:
            loss = loss + param.norm(p=p)  # avoid += to avoid inplace operation

        num_params += 1

    if reduction == "mean":
        loss = loss / num_params

    return loss


def pure_rotation(
    w: torch.Tensor, tune: torch.Tensor, counter_clockwise: bool = False
) -> torch.Tensor:
    # TODO See which clones can be removed
    new_w = torch.empty_like(w)
    complex_w = w[..., 0::2].clone() + 1j * w[..., 1::2].clone()

    if counter_clockwise:
        clockwise_sign = 1
    else:
        clockwise_sign = -1

    complex_w = complex_w * torch.exp(clockwise_sign * 2j * torch.pi * tune)
    new_w[..., 0::2] = complex_w.real.clone()
    new_w[..., 1::2] = complex_w.imag.clone()
    return new_w


def koopman_loss_function(
    model: nn.Module,
    transformed_data: torch.Tensor,
    output: torch.Tensor,
    target: torch.Tensor,
    reduction: str = "mean",
    amplitude_variance_loss: bool = True,
    tune_variance_loss: bool = True,
    weight_decay_l2: bool = False,
) -> torch.Tensor:
    """Loss function for training the Koopman operator model. This function calculates
    the mean squared error (MSE) loss between the output and target tensors, and
    optionally includes additional loss terms for amplitude variance, tune variance,
    and weight decay (L2 regularization).

    The use of these additional loss terms is controlled by the corresponding boolean
    flags. The default values are the recommended settings for training the model. If
    you want to use a different configuration it is recommended to set the flags
    accordingly with `functools.partial`.

    >>> from functools import partial
    >>> loss_fn = partial(koopman_loss_function, amplitude_variance_loss=False)
    >>> loss = loss_fn(model, transformed_data, output, target)

    Parameters
    ----------
    model : nn.Module
        The Koopman operator model being trained.
    transformed_data : torch.Tensor
        The transformed data tensor, which is used to calculate the additional loss
        terms.
    output : torch.Tensor
        The predicted output tensor from the model.
    target : torch.Tensor
        The ground truth target tensor.
    reduction : str, optional
        The reduction method to apply to the loss. It can be either 'mean' or 'sum'.
        If 'mean', the function returns the mean of the loss.
        If 'sum', it returns the sum of the loss. Defaults to 'mean'.
    amplitude_variance_loss : bool, optional
        If True, includes the amplitude variance loss term in the total loss.
        Defaults to True.
    tune_variance_loss : bool, optional
        If True, includes the tune variance loss term in the total loss. Defaults to
        True.
    weight_decay_l2 : bool, optional
        If True, includes the weight decay (L2 regularization) loss term in the total
        loss. Defaults to False.
    """
    mse_loss_value = F.mse_loss(output, target, reduction=reduction)
    amplitude_variance_loss_value = None
    tune_variance_loss_value = None
    weight_decay_l2_value = None

    for transformed_data_i in transformed_data:
        batched_transformed_data_i = transformed_data_i.unsqueeze(0).reshape(
            -1, 2 * model.dim
        )

        if amplitude_variance_loss:
            temp = transformed_amplitude_variance(batched_transformed_data_i)

            if amplitude_variance_loss_value is None:
                amplitude_variance_loss_value = temp.clone()

            else:
                amplitude_variance_loss_value = amplitude_variance_loss_value + temp

        if tune_variance_loss:
            temp = transformed_tune_variance(batched_transformed_data_i)

            if tune_variance_loss_value is None:
                tune_variance_loss_value = temp.clone()

            else:
                tune_variance_loss_value = tune_variance_loss_value + temp

        if weight_decay_l2:
            temp = norm_parameter_loss(model=model, p=2)

            if weight_decay_l2_value is None:
                weight_decay_l2_value = temp.clone()

            else:
                weight_decay_l2_value = weight_decay_l2_value + temp

    loss = mse_loss_value / mse_loss_value.detach()

    if amplitude_variance_loss_value is not None:
        loss = (
            loss
            + amplitude_variance_loss_value / amplitude_variance_loss_value.detach()
        )

    if tune_variance_loss_value is not None:
        loss = loss + tune_variance_loss_value / tune_variance_loss_value.detach()

    if weight_decay_l2_value is not None:
        loss = loss + weight_decay_l2_value / weight_decay_l2_value.detach()

    return loss
