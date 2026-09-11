import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext
from pricing.coupons import CouponCodeRule
from pricing.engine import PricingEngine

class TestCoupons(unittest.TestCase):
    def test_coupon_application(self):
        engine = PricingEngine()
        engine.register_rule(CouponCodeRule({"SAVE50": Decimal("0.50")}))
        item = CartItem(sku="s1", name="Shoe", category="apparel", unit_price=Decimal("100.00"), metadata={"coupon_code": "SAVE50"})
        ctx = PricingContext(customer=CustomerProfile("c1"), items=[item])
        res = engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("50.00"))
import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext
from pricing.coupons import CouponCodeRule
from pricing.engine import PricingEngine

class TestCoupons(unittest.TestCase):
    def test_coupon_application(self):
        engine = PricingEngine()
        engine.register_rule(CouponCodeRule({"SAVE50": Decimal("0.50")}))
        item = CartItem(sku="s1", name="Shoe", category="apparel", unit_price=Decimal("100.00"), metadata={"coupon_code": "SAVE50"})
        ctx = PricingContext(customer=CustomerProfile("c1"), items=[item])
        res = engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("50.00"))
import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext
from pricing.coupons import CouponCodeRule
from pricing.engine import PricingEngine

class TestCoupons(unittest.TestCase):
    def test_coupon_application(self):
        engine = PricingEngine()
        engine.register_rule(CouponCodeRule({"SAVE50": Decimal("0.50")}))
        item = CartItem(sku="s1", name="Shoe", category="apparel", unit_price=Decimal("100.00"), metadata={"coupon_code": "SAVE50"})
        ctx = PricingContext(customer=CustomerProfile("c1"), items=[item])
        res = engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("50.00"))
import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext
from pricing.coupons import CouponCodeRule
from pricing.engine import PricingEngine

class TestCoupons(unittest.TestCase):
    def test_coupon_application(self):
        engine = PricingEngine()
        engine.register_rule(CouponCodeRule({"SAVE50": Decimal("0.50")}))
        item = CartItem(sku="s1", name="Shoe", category="apparel", unit_price=Decimal("100.00"), metadata={"coupon_code": "SAVE50"})
        ctx = PricingContext(customer=CustomerProfile("c1"), items=[item])
        res = engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("50.00"))
import unittest
from decimal import Decimal
from pricing.models import CartItem, CustomerProfile, PricingContext
from pricing.coupons import CouponCodeRule
from pricing.engine import PricingEngine

class TestCoupons(unittest.TestCase):
    def test_coupon_application(self):
        engine = PricingEngine()
        engine.register_rule(CouponCodeRule({"SAVE50": Decimal("0.50")}))
        item = CartItem(sku="s1", name="Shoe", category="apparel", unit_price=Decimal("100.00"), metadata={"coupon_code": "SAVE50"})
        ctx = PricingContext(customer=CustomerProfile("c1"), items=[item])
        res = engine.evaluate(ctx)
        self.assertEqual(res.final_total, Decimal("50.00"))
