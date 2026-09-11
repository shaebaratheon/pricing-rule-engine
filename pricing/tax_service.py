"""
Jurisdiction tax calculation service.
"""
from decimal import Decimal
from typing import Dict
from pricing.models import EvaluationContext

class TaxService:
    RATES: Dict[str, Decimal] = {
        "US-CA": Decimal("0.0925"),
        "US-NY": Decimal("0.08875"),
        "US-TX": Decimal("0.0825"),
        "US-WA": Decimal("0.1010"),
        "DE": Decimal("0.19"),
        "UK": Decimal("0.20"),
    }

    @classmethod
    def calculate_tax(cls, region: str, ctx: EvaluationContext) -> Decimal:
        if ctx.customer.is_tax_exempt:
            ctx.record_step("Customer is tax exempt. Tax is 0.00")
            return Decimal("0.00")
        rate = cls.RATES.get(region, Decimal("0.05"))
        tax = (ctx.net_item_subtotal * rate).quantize(Decimal("0.01"))
        ctx.record_step(f"Calculated tax for region {region} at rate {rate*100}%: ${tax}")
        return tax

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules

# Tax jurisdiction tables and exemption rules
