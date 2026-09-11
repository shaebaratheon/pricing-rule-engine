"""
Dynamic shipping matrix calculation.
"""
from decimal import Decimal
from pricing.models import EvaluationContext

class ShippingCalculator:
    FREE_SHIPPING_THRESHOLD = Decimal("150.00")
    STANDARD_RATE = Decimal("9.99")
    EXPRESS_RATE = Decimal("24.99")

    @classmethod
    def calculate(cls, ctx: EvaluationContext, express: bool = False) -> Decimal:
        if ctx.net_item_subtotal >= cls.FREE_SHIPPING_THRESHOLD and not express:
            ctx.record_step("Order qualified for Free Standard Shipping!")
            return Decimal("0.00")
        if express:
            ctx.record_step(f"Applied Express Shipping: ${cls.EXPRESS_RATE}")
            return cls.EXPRESS_RATE
        ctx.record_step(f"Applied Standard Shipping: ${cls.STANDARD_RATE}")
        return cls.STANDARD_RATE

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables

# Logistics providers and freight rate tables
