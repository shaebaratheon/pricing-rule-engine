"""
Orchestration engine evaluating rules across pipeline stages.
"""
from decimal import Decimal
from typing import List
from pricing.models import PricingContext
from pricing.rules import PricingRule

class PricingEngine:
    def __init__(self):
        self._rules: List[PricingRule] = []

    def register_rule(self, rule: PricingRule) -> None:
        self._rules.append(rule)
        self._rules.sort(key=lambda r: r.priority.value, reverse=True)

    def evaluate(self, context: PricingContext) -> PricingContext:
        context.log(f"Starting pricing evaluation with {len(self._rules)} registered rules.")
        for rule in self._rules:
            if rule.is_eligible(context):
                context.log(f"Rule {rule.rule_id} is eligible. Executing.")
                rule.apply(context)
            else:
                context.log(f"Rule {rule.rule_id} skipped (not eligible).")
        context.log(f"Evaluation complete. Subtotal: {context.original_subtotal}, Total: {context.final_total}")
        return context
