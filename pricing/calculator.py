"""
Evaluation pipeline driver coordinating multi-stage rule execution.
"""
from typing import List
from pricing.models import EvaluationContext
from pricing.rules import BaseRule

class PricingPipeline:
    def __init__(self):
        self._rules: List[BaseRule] = []

    def add_rule(self, rule: BaseRule) -> None:
        self._rules.append(rule)
        self._rules.sort(key=lambda r: r.stage.value)

    def run(self, ctx: EvaluationContext) -> EvaluationContext:
        ctx.record_step(f"Starting pricing pipeline with {len(self._rules)} active rules")
        for rule in self._rules:
            if rule.evaluate(ctx):
                ctx.record_step(f"Rule [{rule.rule_id}] triggered.")
                rule.apply(ctx)
            else:
                ctx.record_step(f"Rule [{rule.rule_id}] skipped.")
        ctx.record_step(f"Pricing pipeline completed. Grand total: {ctx.grand_total}")
        return ctx

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks

# Pipeline validation and metrics hooks
