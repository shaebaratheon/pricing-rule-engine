"""
Core pricing rules and discount calculation logic.
"""
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional
from pricing.models import CartItem, CustomerProfile, DiscountType, PricingContext, RulePriority, TierLevel

class PricingRule(ABC):
    def __init__(self, rule_id: str, name: str, priority: RulePriority = RulePriority.NORMAL):
        self.rule_id = rule_id
        self.name = name
        self.priority = priority

    @abstractmethod
    def is_eligible(self, context: PricingContext) -> bool:
        pass

    @abstractmethod
    def apply(self, context: PricingContext) -> None:
        pass

class TierLoyaltyDiscountRule(PricingRule):
    TIER_RATES = {
        TierLevel.BRONZE: Decimal("0.00"),
        TierLevel.SILVER: Decimal("0.05"),
        TierLevel.GOLD: Decimal("0.10"),
        TierLevel.PLATINUM: Decimal("0.15"),
    }

    def __init__(self, rule_id: str = "RULE_TIER_DISCOUNT"):
        super().__init__(rule_id, "Customer Tier Loyalty Discount", RulePriority.NORMAL)

    def is_eligible(self, context: PricingContext) -> bool:
        rate = self.TIER_RATES.get(context.customer.tier, Decimal("0.00"))
        return rate > Decimal("0.00")

    def apply(self, context: PricingContext) -> None:
        rate = self.TIER_RATES[context.customer.tier]
        context.log(f"Applying {self.name} for tier {context.customer.tier.value} at rate {rate*100}%")
        for item in context.items:
            discount = (item.unit_price * rate * Decimal(item.quantity)).quantize(Decimal("0.01"))
            item.applied_discounts.append(discount)
        context.applied_rule_ids.append(self.rule_id)

class VolumeThresholdRule(PricingRule):
    def __init__(self, rule_id: str = "RULE_VOL_THRESHOLD", min_spend: Decimal = Decimal("100.00"), flat_discount: Decimal = Decimal("15.00")):
        super().__init__(rule_id, "Volume Spend Threshold Discount", RulePriority.LOW)
        self.min_spend = min_spend
        self.flat_discount = flat_discount

    def is_eligible(self, context: PricingContext) -> bool:
        return context.original_subtotal >= self.min_spend

    def apply(self, context: PricingContext) -> None:
        context.log(f"Applying {self.name} of ${self.flat_discount} on subtotal ${context.original_subtotal}")
        if context.items:
            context.items[0].applied_discounts.append(self.flat_discount)
        context.applied_rule_ids.append(self.rule_id)

class CategoryClearanceRule(PricingRule):
    def __init__(self, target_category: str, discount_rate: Decimal, rule_id: str = "RULE_CAT_CLEARANCE"):
        super().__init__(rule_id, f"Clearance Discount for {target_category}", RulePriority.HIGH)
        self.target_category = target_category
        self.discount_rate = discount_rate

    def is_eligible(self, context: PricingContext) -> bool:
        return any(item.category == self.target_category for item in context.items)

    def apply(self, context: PricingContext) -> None:
        context.log(f"Applying {self.name} to category '{self.target_category}'")
        for item in context.items:
            if item.category == self.target_category:
                discount = (item.unit_price * self.discount_rate * Decimal(item.quantity)).quantize(Decimal("0.01"))
                item.applied_discounts.append(discount)
        context.applied_rule_ids.append(self.rule_id)
