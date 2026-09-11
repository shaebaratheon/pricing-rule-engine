"""
Domain models for items, customers, discounts, and pricing contexts.
"""
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Set

class TierLevel(Enum):
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

class RulePriority(Enum):
    LOW = 10
    NORMAL = 50
    HIGH = 100
    CRITICAL = 200

class DiscountType(Enum):
    PERCENTAGE = "PERCENTAGE"
    FLAT_AMOUNT = "FLAT_AMOUNT"
    FIXED_PRICE = "FIXED_PRICE"
    BUY_X_GET_Y = "BUY_X_GET_Y"

@dataclass(frozen=True)
class CustomerProfile:
    customer_id: str
    tier: TierLevel = TierLevel.BRONZE
    lifetime_spend: Decimal = Decimal("0.00")
    account_created_at: datetime = field(default_factory=datetime.utcnow)
    tags: Set[str] = field(default_factory=set)
    is_employee: bool = False

@dataclass
class CartItem:
    sku: str
    name: str
    category: str
    unit_price: Decimal
    quantity: int = 1
    applied_discounts: List[Decimal] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    @property
    def line_subtotal(self) -> Decimal:
        return self.unit_price * Decimal(self.quantity)

    @property
    def final_line_total(self) -> Decimal:
        discount_sum = sum(self.applied_discounts, Decimal("0.00"))
        return max(Decimal("0.00"), self.line_subtotal - discount_sum)

@dataclass
class PricingContext:
    customer: CustomerProfile
    items: List[CartItem]
    currency: str = "USD"
    evaluated_at: datetime = field(default_factory=datetime.utcnow)
    applied_rule_ids: List[str] = field(default_factory=list)
    audit_trail: List[str] = field(default_factory=list)

    @property
    def original_subtotal(self) -> Decimal:
        return sum((item.line_subtotal for item in self.items), Decimal("0.00"))

    @property
    def total_discount(self) -> Decimal:
        return sum((sum(item.applied_discounts, Decimal("0.00")) for item in self.items), Decimal("0.00"))

    @property
    def final_total(self) -> Decimal:
        return sum((item.final_line_total for item in self.items), Decimal("0.00"))

    def log(self, message: str) -> None:
        self.audit_trail.append(f"[{datetime.utcnow().isoformat()}] {message}")
