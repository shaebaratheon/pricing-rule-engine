"""
Unit tests validating pricing calculation scenarios.
"""
import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext, TierLevel
from pricing.rules import CategoryClearanceRule, TierLoyaltyDiscountRule, VolumeThresholdRule
from pricing.engine import PricingEngine

class TestPricingEngine(unittest.TestCase):
    def setUp(self):
        self.engine = PricingEngine()
        self.engine.register_rule(TierLoyaltyDiscountRule())
        self.engine.register_rule(VolumeThresholdRule(min_spend=Decimal("100.00"), flat_discount=Decimal("10.00")))
        self.engine.register_rule(CategoryClearanceRule("books", Decimal("0.20")))

    def test_bronze_customer_no_tier_discount(self):
        customer = CustomerProfile(customer_id="c_001", tier=TierLevel.BRONZE)
        item = CartItem(sku="sku_1", name="Python Book", category="books", unit_price=Decimal("50.00"), quantity=1)
        ctx = PricingContext(customer=customer, items=[item])
        res = self.engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("40.00")) # 20% off books

    def test_gold_customer_stacked_discounts(self):
        customer = CustomerProfile(customer_id="c_002", tier=TierLevel.GOLD)
        item1 = CartItem(sku="sku_2", name="Laptop Bag", category="accessories", unit_price=Decimal("80.00"), quantity=1)
        item2 = CartItem(sku="sku_3", name="Wireless Mouse", category="accessories", unit_price=Decimal("30.00"), quantity=1)
        ctx = PricingContext(customer=customer, items=[item1, item2])
        res = self.engine.evaluate(ctx)
        # Subtotal: 110.00
        # Tier 10%: 8.00 + 3.00 = 11.00
        # Vol Threshold (>100): 10.00
        # Total discount: 21.00 -> final: 89.00
        self.assertEqual(res.original_subtotal, Decimal("110.00"))
        self.assertEqual(res.final_total, Decimal("89.00"))

if __name__ == "__main__":
    unittest.main()
