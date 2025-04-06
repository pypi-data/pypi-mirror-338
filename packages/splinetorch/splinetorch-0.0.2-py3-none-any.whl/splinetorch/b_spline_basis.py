import torch

def b_spline_basis(x: torch.Tensor, knots: torch.Tensor, degree: int, return_all: bool = False) -> torch.Tensor:
    r"""
    Compute B-spline basis functions of a given degree at specified points.

    Parameters
    ----------
    x : torch.Tensor
        The input points where the basis functions are evaluated.
        Should be a 1D tensor.
    knots : torch.Tensor
        The non-decreasing sequence of knots defining the B-spline.
        Should be a 1D tensor with values in [0, 1].
        For proper boundary behavior, the knot sequence should typically include
        (degree + 1) repeated knots at each end (clamped B-spline).
    degree : int
        The degree of the B-spline basis functions (non-negative integer).
    return_all : bool, optional
        If True, returns all basis functions up to the specified degree.

    Returns
    -------
    torch.Tensor
        A 2D tensor of shape (len(x), n_bases) where each column corresponds to a B-spline
        basis function evaluated at the points in `x`. The basis functions sum to 1 at each point.

    Notes
    -----
    The number of B-spline basis functions, :math:`n_{\text{bases}}`, is determined
    by the number of interior knots :math:`n` and the degree :math:`p`:

    .. math::

        n_{\text{bases}} = n + p + 1

    where :math:`n` is len(knots).

    The basis functions are computed using the Cox-de Boor recursion formula.

    **Cox-de Boor recursion formula:**

    The B-spline basis functions of degree :math:`p` are defined recursively as:

    **Base case (degree 0):**

    .. math::

        N_{i,0}(x) =
        \begin{cases}
            1, & \text{if } t_i \leq x \leq t_{i+1}, \\
            0, & \text{otherwise}.
        \end{cases}

    **Recursive case:**

    For degrees :math:`p \geq 1`:

    .. math::

        N_{i,p}(x) = \frac{x - t_i}{t_{i+p} - t_i} N_{i,p-1}(x) + \frac{t_{i+p+1} - x}{t_{i+p+1} - t_{i+1}} N_{i+1,p-1}(x)

    If a denominator is zero, the corresponding term is defined to be zero.

    Examples
    --------
    >>> import torch
    >>> x = torch.linspace(0, 1, 5)  # [0.00, 0.25, 0.50, 0.75, 1.00]
    >>> knots = torch.tensor([0, 0.2, 0.4, 0.6, 0.8, 1])
    >>> degree = 2
    >>> basis = b_spline_basis(x, knots, degree)
    >>> print(basis.shape) # 5 points, 7 basis functions (n + p + 1 = 4 + 2 + 1)
    >>> torch.allclose(basis.sum(dim=1), torch.ones(5))  # Sum to 1
    """
    # Input validation
    if degree < 0:
        raise ValueError("Degree must be non-negative")

    if not torch.all(knots[1:] >= knots[:-1]):
        raise ValueError("Knots must be in non-decreasing order")

    if torch.any(knots < 0) or torch.any(knots > 1):
        raise ValueError("Knots must be in the interval [0, 1]")

    # Ensure knots are on same device as input x
    device = x.device
    knots = knots.to(device)

    # Match input dtype
    dtype = x.dtype
    n_knots = len(knots)
    n_bases = n_knots - degree - 1

    # Initialize the basis functions matrix for all degrees
    # basis = torch.zeros((degree + 1, n_points, n_bases + degree), dtype=dtype, device=device)

    # Initialize degree 0 basis functions
    degree0 = []
    for j in range(n_knots - 1):
        if j < n_knots - degree - 2:
            mask = (knots[j] <= x) & (x < knots[j + 1])
        else:
            # For the last interval, include the right endpoint
            mask = (knots[j] <= x) & (x <= knots[j + 1])
        degree0.append(mask.to(dtype))

    basis_prev = torch.stack(degree0, dim=-1)
    all_degrees = [basis_prev]

    # Add numerical stability threshold
    eps = 1e-10
    # Compute basis functions for higher degrees
    for p in range(1, degree + 1):
        current_list  = []
        for j in range(n_knots - p - 1):
            # Left term
            denom1 = knots[j + p] - knots[j]
            left = torch.zeros_like(x, dtype=dtype, device=device)
            if denom1 > eps:
                left = (x - knots[j]) / denom1 * basis_prev[..., j]

            # Right term
            denom2 = knots[j + p + 1] - knots[j + 1]
            right = torch.zeros_like(x, dtype=dtype, device=device)
            if denom2 > eps:
                right = (knots[j + p + 1] - x) / denom2 * basis_prev[..., j+1]

            current_list .append(left + right)
        basis_prev = torch.stack(current_list, dim=-1)  # shape: (n_points, n_knots - p - 1)
        all_degrees.append(basis_prev)

    if return_all:
        padded_degrees = []
        for deg_basis in all_degrees:
            cur_len = deg_basis.shape[-1]
            if cur_len < (n_knots - 1):
                pad_amt = n_knots - 1 - cur_len
                # pad last dimension (pad_left=0, pad_right=pad_amt)
                deg_basis = torch.nn.functional.pad(deg_basis, (0, pad_amt))
            padded_degrees.append(deg_basis)
        # Stack along a new dimension: shape becomes (degree+1, n_points, full_basis_len)
        result = torch.stack(padded_degrees, dim=0)
    else:
        # Return only the highest degree, sliced to match original behavior: (n_points, n_bases)
        result = basis_prev[..., :n_bases]

    return result

def b_spline_basis_derivative(x: torch.Tensor, knots: torch.Tensor, degree: int, order: int) -> torch.Tensor:
    """Compute the derivative of B-spline basis functions.

    Parameters
    ----------
    x : torch.Tensor
        Points at which to evaluate the derivative. Should be a 1D tensor.
    knots : torch.Tensor
        The knot sequence defining the B-spline. Should be a 1D tensor with values in [0, 1].
    degree : int
        The degree of the B-spline basis functions (non-negative integer).
    order : int
        Order of the derivative to compute. Must be non-negative.
        If greater than degree, returns zeros.

    Returns
    -------
    torch.Tensor
        A 2D tensor of shape (len(x), n_bases) containing the derivative values
        of each basis function at the specified points.
    """
    if order == 0:
        return b_spline_basis(x, knots, degree)

    if order > degree:
        batch_shape = x.shape[:-1] if x.ndim > 1 else ()
        n_points = x.shape[-1] if x.ndim > 1 else x.shape[0]
        n_bases = len(knots) - degree - 1
        return torch.zeros(batch_shape + (n_points, n_bases), dtype=x.dtype, device=x.device)

    eps = 1e-6
    x_adj = torch.where(x == knots[-1], x - eps, x)
    original_ndim = x_adj.ndim

    # Ensure x is batched (if it isn't, add a batch dim)
    if x_adj.ndim == 1:
        x_adj = x_adj.unsqueeze(0)

    batch_shape = x_adj.shape[:-1]
    n_points = x_adj.shape[-1]
    n_bases = len(knots) - degree - 1

    if order == 1:
        basis = b_spline_basis(x_adj, knots, degree - 1)  # shape: batch_shape + (n_points, len(knots)-degree)

        denom1 = knots[degree:degree+n_bases] - knots[:n_bases]
        denom2 = knots[degree+1:degree+n_bases+1] - knots[1:n_bases+1]
        valid_denom1 = denom1 > 1e-10
        valid_denom2 = denom2 > 1e-10

        result = torch.zeros(batch_shape + (n_points, n_bases), dtype=x.dtype, device=x.device)

        # For vmap compatibility - handle arbitrary batch dimensions
        # Create properly expanded masks for broadcasting
        expanded_valid_denom1 = valid_denom1.view(*([1] * len(batch_shape)), 1, -1)
        expanded_valid_denom2 = valid_denom2.view(*([1] * len(batch_shape)), 1, -1)

        # Create expanded denominators for broadcasting
        expanded_denom1 = denom1.view(*([1] * len(batch_shape)), 1, -1)
        expanded_denom2 = denom2.view(*([1] * len(batch_shape)), 1, -1)

        # Apply the operations using broadcasting
        term1 = torch.zeros_like(result)
        term2 = torch.zeros_like(result)

        # First term: degree * basis[..., :-1] / denom1
        basis_term1 = basis[..., :-1]
        term1 = torch.where(
            expanded_valid_denom1,
            degree * basis_term1 / expanded_denom1,
            torch.zeros_like(term1)
        )

        # Second term: -degree * basis[..., 1:] / denom2
        basis_term2 = basis[..., 1:]
        term2 = torch.where(
            expanded_valid_denom2,
            -degree * basis_term2 / expanded_denom2,
            torch.zeros_like(term2)
        )

        result = term1 + term2

        # If the input was not batched, remove the batch dimension to maintain the same shape
        if original_ndim == 1:
            result = result.squeeze(0)

        return result

    # For higher order, recursively call derivative (with similar adjustments)
    result = degree * (
        _div_or_zero(
            b_spline_basis_derivative(x_adj, knots, degree-1, order-1)[..., :-1],
            knots[degree:degree+n_bases] - knots[:n_bases]
        ) -
        _div_or_zero(
            b_spline_basis_derivative(x_adj, knots, degree-1, order-1)[..., 1:],
            knots[degree+1:degree+n_bases+1] - knots[1:n_bases+1]
        )
    )

    # If the input was not batched, remove the batch dimension to maintain the same shape
    if original_ndim == 1:
        result = result.squeeze(0)

    return result

def _div_or_zero(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Safe division that returns 0 when denominator is too small."""
    # Update to handle arbitrary batch dimensions
    # Expand b to match a's batch dimensions
    if b.ndim < a.ndim:
        # Add necessary batch dimensions to b
        expand_dims = [1] * (a.ndim - b.ndim - 1) + [b.shape[0]]
        b_expanded = b.view(*expand_dims)
        mask = b_expanded > 1e-10
    else:
        mask = b > 1e-10
        b_expanded = b

    result = torch.zeros_like(a)
    # Use torch.where for safe broadcasting
    result = torch.where(mask, a / b_expanded, torch.zeros_like(a))
    return result
