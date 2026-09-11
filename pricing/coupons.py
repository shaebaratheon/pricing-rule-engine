"""
Promotional coupon code engine with expiry date and usage quota validation.
"""
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional
from pricing.enums import CalculationStage
from pricing.models import EvaluationContext
from pricing.rules import BaseRule

@dataclass(frozen=True)
class CouponSpec:
    code: str
    discount_percentage: Decimal
    min_spend: Decimal
    expires_at: datetime
    max_uses: int
    current_uses: int = 0

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at

    @property
    def is_quota_exceeded(self) -> bool:
        return self.current_uses >= self.max_uses

class CouponRule(BaseRule):
    def __init__(self, coupon_repo: Dict[str, CouponSpec]):
        super().__init__("RULE_COUPON_PROMO", "Promotional Coupon Code Application", CalculationStage.PROMOTIONAL_CODE)
        self.coupon_repo = coupon_repo

    def evaluate(self, ctx: EvaluationContext) -> bool:
        code = None
        for item in ctx.items:
            if "coupon_code" in item.attributes:
                code = item.attributes["coupon_code"]
                break
        if not code or code not in self.coupon_repo:
            return False
        spec = self.coupon_repo[code]
        if spec.is_expired or spec.is_quota_exceeded:
            ctx.record_step(f"Coupon '{code}' is expired or usage quota exhausted.")
            return False
        if ctx.net_item_subtotal < spec.min_spend:
            ctx.record_step(f"Subtotal {ctx.net_item_subtotal} does not meet coupon minimum spend {spec.min_spend}.")
            return False
        return True

    def apply(self, ctx: EvaluationContext) -> None:
        code = next(item.attributes["coupon_code"] for item in ctx.items if "coupon_code" in item.attributes)
        spec = self.coupon_repo[code]
        rate = spec.discount_percentage
        ctx.record_step(f"Redeeming coupon '{code}' with {rate*100}% off net item subtotal")
        for item in ctx.items:
            disc = (item.net_total * rate).quantize(Decimal("0.01"))
            item.applied_discounts.append(disc)
        ctx.applied_rule_ids.append(self.rule_id)

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging

# Coupon audit and analytics logging
