def apply_discount(price_cents: int, rate: float) -> int:
    """Return the price after a fractional discount, e.g. rate=0.15 for 15% off."""
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")
    return round(price_cents * (1 - rate))
