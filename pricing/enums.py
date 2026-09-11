"""
Pricing and promotional enumeration types.
"""
from enum import Enum

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CAD = "CAD"
    AUD = "AUD"

class TierLevel(Enum):
    STANDARD = "STANDARD"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
    DIAMOND = "DIAMOND"

class DiscountScope(Enum):
    ORDER = "ORDER"
    LINE_ITEM = "LINE_ITEM"
    SHIPPING = "SHIPPING"
    TAX = "TAX"

class CalculationStage(Enum):
    PRE_EVALUATION = 0
    CATALOG_BASE = 10
    TIER_LOYALTY = 20
    VOLUME_DISCOUNT = 30
    PROMOTIONAL_CODE = 40
    CUSTOM_OVERRIDE = 50
    POST_ADJUSTMENT = 60

class RoundingMode(Enum):
    HALF_EVEN = "HALF_EVEN"
    HALF_UP = "HALF_UP"
    FLOOR = "FLOOR"
    CEIL = "CEIL"

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations

# Additional configuration enumerations
