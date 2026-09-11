# Pricing Rule Engine

A production-grade, extensible pricing and promotion pipeline written in Python.

## Architecture
- **Models**: Immutable customer profiles, mutable cart items with line-level discount tracking.
- **Rules**: Priority-staged rules (Catalog clearance, Tier loyalty, Volume thresholds, Coupon codes).
- **Tax & Shipping**: Independent domain calculators integrated into the checkout context.
- **Auditability**: Complete chronological trace logging of all discount evaluations.

## Usage
```python
from pricing.calculator import PricingPipeline
from pricing.models import CartItem, CustomerProfile, EvaluationContext

pipeline = PricingPipeline()
ctx = EvaluationContext(customer=..., items=[...])
result = pipeline.run(ctx)
print("Final total:", result.grand_total)
```

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples

# Documentation & examples
