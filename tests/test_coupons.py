"""
Unit tests for the CouponRule and CouponSpec validations.
"""
import unittest
from datetime import datetime, timedelta
from decimal import Decimal
from pricing.enums import TierLevel
from pricing.models import CartItem, CustomerProfile, EvaluationContext
from pricing.coupons import CouponRule, CouponSpec
from pricing.calculator import PricingPipeline

class TestCouponEngine(unittest.TestCase):
    def setUp(self):
        self.coupons = {
            "SAVE20": CouponSpec(
                code="SAVE20",
                discount_percentage=Decimal("0.20"),
                min_spend=Decimal("50.00"),
                expires_at=datetime.utcnow() + timedelta(days=30),
                max_uses=100
            ),
            "EXPIRED10": CouponSpec(
                code="EXPIRED10",
                discount_percentage=Decimal("0.10"),
                min_spend=Decimal("10.00"),
                expires_at=datetime.utcnow() - timedelta(days=1),
                max_uses=10
            )
        }
        self.pipeline = PricingPipeline()
        self.pipeline.add_rule(CouponRule(self.coupons))

    def test_valid_coupon_applied(self):
        cust = CustomerProfile(customer_id="c1", email="c1@example.com")
        item = CartItem(sku="SKU_99", title="Book", category="books", unit_price=Decimal("100.00"), attributes={"coupon_code": "SAVE20"})
        ctx = EvaluationContext(customer=cust, items=[item])
        res = self.pipeline.run(ctx)
        self.assertIn("RULE_COUPON_PROMO", res.applied_rule_ids)
        self.assertEqual(res.net_item_subtotal, Decimal("80.00"))

    def test_expired_coupon_rejected(self):
        cust = CustomerProfile(customer_id="c2", email="c2@example.com")
        item = CartItem(sku="SKU_98", title="Pen", category="office", unit_price=Decimal("20.00"), attributes={"coupon_code": "EXPIRED10"})
        ctx = EvaluationContext(customer=cust, items=[item])
        res = self.pipeline.run(ctx)
        self.assertNotIn("RULE_COUPON_PROMO", res.applied_rule_ids)
        self.assertEqual(res.net_item_subtotal, Decimal("20.00"))

if __name__ == "__main__":
    unittest.main()

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites

# Coupon edge case test suites
