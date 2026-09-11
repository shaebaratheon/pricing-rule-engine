"""
Declarative pricing rules and rule engines.
"""
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional
from pricing.enums import CalculationStage, TierLevel
from pricing.models import CartItem, EvaluationContext

class BaseRule(ABC):
    def __init__(self, rule_id: str, title: str, stage: CalculationStage):
        self.rule_id = rule_id
        self.title = title
        self.stage = stage

    @abstractmethod
    def evaluate(self, ctx: EvaluationContext) -> bool:
        pass

    @abstractmethod
    def apply(self, ctx: EvaluationContext) -> None:
        pass

class TierLoyaltyRule(BaseRule):
    DISCOUNT_MAP = {
        TierLevel.STANDARD: Decimal("0.00"),
        TierLevel.BRONZE: Decimal("0.02"),
        TierLevel.SILVER: Decimal("0.05"),
        TierLevel.GOLD: Decimal("0.10"),
        TierLevel.PLATINUM: Decimal("0.15"),
        TierLevel.DIAMOND: Decimal("0.20"),
    }

    def __init__(self):
        super().__init__("RULE_TIER_LOYALTY", "Customer Tier Loyalty Discount", CalculationStage.TIER_LOYALTY)

    def evaluate(self, ctx: EvaluationContext) -> bool:
        rate = self.DISCOUNT_MAP.get(ctx.customer.tier, Decimal("0.00"))
        return rate > Decimal("0.00")

    def apply(self, ctx: EvaluationContext) -> None:
        rate = self.DISCOUNT_MAP[ctx.customer.tier]
        ctx.record_step(f"Applying loyalty discount of {rate*100}% for tier {ctx.customer.tier.value}")
        for item in ctx.items:
            disc = (item.unit_price * rate * Decimal(item.quantity)).quantize(Decimal("0.01"))
            item.applied_discounts.append(disc)
        ctx.applied_rule_ids.append(self.rule_id)

class VolumeThresholdRule(BaseRule):
    def __init__(self, threshold: Decimal, discount_amount: Decimal):
        super().__init__("RULE_VOLUME_SPEND", "Volume Spend Threshold Reduction", CalculationStage.VOLUME_DISCOUNT)
        self.threshold = threshold
        self.discount_amount = discount_amount

    def evaluate(self, ctx: EvaluationContext) -> bool:
        return ctx.original_subtotal >= self.threshold

    def apply(self, ctx: EvaluationContext) -> None:
        ctx.record_step(f"Subtotal {ctx.original_subtotal} qualifies for volume threshold {self.threshold}. Reducing {self.discount_amount}")
        if ctx.items:
            ctx.items[0].applied_discounts.append(self.discount_amount)
        ctx.applied_rule_ids.append(self.rule_id)

class CategoryClearanceRule(BaseRule):
    def __init__(self, target_category: str, discount_rate: Decimal):
        super().__init__(f"RULE_CLEARANCE_{target_category.upper()}", f"Clearance on {target_category}", CalculationStage.CATALOG_BASE)
        self.target_category = target_category
        self.discount_rate = discount_rate

    def evaluate(self, ctx: EvaluationContext) -> bool:
        return any(item.category == self.target_category for item in ctx.items)

    def apply(self, ctx: EvaluationContext) -> None:
        ctx.record_step(f"Applying clearance rate {self.discount_rate*100}% to category '{self.target_category}'")
        for item in ctx.items:
            if item.category == self.target_category:
                disc = (item.unit_price * self.discount_rate * Decimal(item.quantity)).quantize(Decimal("0.01"))
                item.applied_discounts.append(disc)
        ctx.applied_rule_ids.append(self.rule_id)

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions

# Specialized domain rule definitions
