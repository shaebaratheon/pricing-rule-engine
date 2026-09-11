"""
Rich data structures representing customers, cart items, tax tables, and evaluation contexts.
"""
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP
from typing import Dict, List, Optional, Set
from pricing.enums import Currency, TierLevel, DiscountScope, RoundingMode

@dataclass(frozen=True)
class CustomerProfile:
    customer_id: str
    email: str
    tier: TierLevel = TierLevel.STANDARD
    lifetime_spend: Decimal = Decimal("0.00")
    total_orders_placed: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    tags: Set[str] = field(default_factory=set)
    is_vip: bool = False
    is_tax_exempt: bool = False
    country_code: str = "US"

@dataclass
class CartItem:
    sku: str
    title: str
    category: str
    unit_price: Decimal
    quantity: int = 1
    applied_discounts: List[Decimal] = field(default_factory=list)
    attributes: Dict[str, str] = field(default_factory=dict)
    weight_kg: float = 0.0

    @property
    def gross_subtotal(self) -> Decimal:
        return (self.unit_price * Decimal(self.quantity)).quantize(Decimal("0.01"))

    @property
    def total_discounts(self) -> Decimal:
        return sum(self.applied_discounts, Decimal("0.00")).quantize(Decimal("0.01"))

    @property
    def net_total(self) -> Decimal:
        return max(Decimal("0.00"), self.gross_subtotal - self.total_discounts)

@dataclass
class EvaluationContext:
    customer: CustomerProfile
    items: List[CartItem]
    currency: Currency = Currency.USD
    evaluated_at: datetime = field(default_factory=datetime.utcnow)
    applied_rule_ids: List[str] = field(default_factory=list)
    audit_logs: List[str] = field(default_factory=list)
    shipping_cost: Decimal = Decimal("0.00")
    estimated_tax: Decimal = Decimal("0.00")

    @property
    def original_subtotal(self) -> Decimal:
        return sum((item.gross_subtotal for item in self.items), Decimal("0.00"))

    @property
    def total_item_discounts(self) -> Decimal:
        return sum((item.total_discounts for item in self.items), Decimal("0.00"))

    @property
    def net_item_subtotal(self) -> Decimal:
        return sum((item.net_total for item in self.items), Decimal("0.00"))

    @property
    def grand_total(self) -> Decimal:
        return self.net_item_subtotal + self.shipping_cost + self.estimated_tax

    def record_step(self, message: str) -> None:
        ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.audit_logs.append(f"[{ts}] {message}")

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions

# Model utility functions
