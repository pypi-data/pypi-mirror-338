[![tests](https://github.com/joakimwallmark/irtorch/actions/workflows/tests.yml/badge.svg)](https://github.com/joakimwallmark/irtorch/actions/workflows/tests.yml)

# SplineTorch

SplineTorch is a Python package for fitting splines in PyTorch. Spline with enforced and/or penalized constraints are supported.

## Installation

```bash
pip install splinetorch
```

## Features

- Univariate and multivariate B-spline regression
- Binary and categorical classification
- Probability density function (PDF) fitting
- Constraint support:
  - Derivative constraints (e.g., monotonicity, convexity)
  - Point constraints
  - PDF constraints (non-negativity and integration to 1)

## Examples

### Simple Univariate Regression

```python
import torch
from splinetorch.b_spline import BSpline

x = torch.linspace(0, 1, 100).view(-1, 1)
y = torch.sin(2 * torch.pi * x) + torch.randn_like(x) * 0.1
spline = BSpline(x=x, y=y)
spline.fit(x, y)
y_pred = spline.predict(x)
spline.plot_fit(x, y)
```

### Binary Classification with monotonely increasing logit

```python
import torch
from splinetorch.b_spline import BSpline

x = torch.linspace(-3, 3, 100).view(-1, 1)
y = (torch.sin(2.2 * torch.pi * x) > 0).float()

# Force monotone increasing logit
derivative_constraints = {1: {'>': torch.tensor(0.0)}}  # 1st derivative > 0
spline = BSpline(x=x, y=y, output_type="binary")
spline.fit(x, y, derivative_constraints=derivative_constraints)
probabilities = spline.predict(x)
spline.plot_fit(x, y)
```

### Multivariate Regression with Point Constraints

```python
import torch
from splinetorch.b_spline import BSpline

x = torch.rand(1000, 2)  # 2D input
y = torch.sum(2*x**2, dim=1).view(-1, 1) - 2
# Constrain degree 0 derivative (the function itself). In the example we want both x values of 0 to return 0.
point_constraints = { 0: {'=': (torch.tensor([[0.0, 0.0]]), torch.tensor([[0.0]]))} }
spline = BSpline(x=x, y=y)
spline.fit(x, y, point_constraints=point_constraints)
y_pred = spline.predict(x)
# Verify the constraint at (0,0)
test_point = torch.tensor([[0.0, 0.0]])
predicted_value = spline.predict(test_point)
print(f"Value at (0,0): {predicted_value.item():.6f}")
```

### PDF Fitting with Constraints (encourage integration to 1 within the interval)

```python
import torch
from splinetorch.b_spline import BSpline

x = torch.linspace(0, 1, 1000).view(-1, 1)
y = torch.exp(-((x - 0.5)**2) / 0.1).view(-1, 1)  # Shape: (n, 1)
spline = BSpline(x=x, y=y)
spline.fit(x, y, pdf_constraint=True)  # Non-negative and integrates to 1
density = spline.predict(x)
spline.plot_fit(x, y)
```

### Three class classification

```python
import torch
from splinetorch.b_spline import BSpline
import numpy as np
import matplotlib.pyplot as plt

x = torch.rand(300, 2)  # 2D input
distances = torch.sum(x**2, dim=1)
y = torch.zeros(len(x), dtype=torch.long)
y[distances < 0.5] = 0
y[(distances >= 0.5) & (distances < 1.0)] = 1
y[distances >= 1.0] = 2

# Fit the spline
spline = BSpline(x=x, y=y, output_type="categorical")
spline.fit(x, y)

# Create a grid of points and get predictions
grid_size = 100
x1_min, x1_max = 0, 1
x2_min, x2_max = 0, 1
x1_grid, x2_grid = np.meshgrid(np.linspace(x1_min, x1_max, grid_size), np.linspace(x2_min, x2_max, grid_size))
grid_points = torch.tensor(np.column_stack([x1_grid.ravel(), x2_grid.ravel()]), dtype=torch.float32)
probs = spline.predict(grid_points)
predictions = probs.argmax(dim=1).numpy()

# Plot decision boundaries
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
axes = axes.ravel()
predictions_2d = predictions.reshape(grid_size, grid_size)
im = axes[0].contourf(x1_grid, x2_grid, predictions_2d, levels=np.arange(4)-0.5, cmap='viridis')
scatter = axes[0].scatter(x[:, 0], x[:, 1], c=y, cmap='viridis', edgecolor='black', s=50)
axes[0].set_title('Decision Boundaries')
axes[0].set_xlabel('X1')
axes[0].set_ylabel('X2')
plt.colorbar(im, ax=axes[0], label='Class')

# Plot probability landscapes for each class
for i in range(3):
    class_probs = probs[:, i].numpy().reshape(grid_size, grid_size)
    im = axes[i+1].contourf(x1_grid, x2_grid, class_probs, levels=20, cmap='RdYlBu')
    # Plot points belonging to this class
    class_mask = (y == i)
    axes[i+1].scatter(x[class_mask, 0], x[class_mask, 1], color='black', 
                     edgecolor='white', s=50, label=f'Class {i} points')
    axes[i+1].set_title(f'Class {i} Probability')
    axes[i+1].set_xlabel('X1')
    axes[i+1].set_ylabel('X2')
    plt.colorbar(im, ax=axes[i+1], label='Probability')
    axes[i+1].legend()

plt.tight_layout()
plt.show()

# Print classification accuracy
class_probs = spline.predict(x)
_, predictions = class_probs.max(dim=1)
accuracy = (predictions == y).float().mean()
print(f"Classification accuracy: {accuracy:.3f}")
```

## License

MIT




