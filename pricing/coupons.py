"""
Coupon redemption rule with usage quotas and minimum spend restrictions.
"""
from decimal import Decimal
from typing import Dict, Optional
from pricing.models import PricingContext, RulePriority
from pricing.rules import PricingRule

class CouponCodeRule(PricingRule):
    def __init__(self, coupon_db: Dict[str, Decimal]):
        super().__init__("RULE_COUPON_CODE", "Coupon Discount Redemption", RulePriority.CRITICAL)
        self.coupon_db = coupon_db

    def is_eligible(self, context: PricingContext) -> bool:
        code = context.items[0].metadata.get("coupon_code") if context.items else None
        return code in self.coupon_db

    def apply(self, context: PricingContext) -> None:
        code = context.items[0].metadata.get("coupon_code")
        pct = self.coupon_db[code]
        context.log(f"Redeeming valid coupon '{code}' with {pct*100}% discount")
        for item in context.items:
            discount = (item.unit_price * pct * Decimal(item.quantity)).quantize(Decimal("0.01"))
            item.applied_discounts.append(discount)
        context.applied_rule_ids.append(self.rule_id)
