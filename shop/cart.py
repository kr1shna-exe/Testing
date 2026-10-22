from shop.pricing import apply_discount


def cart_total(items: list[dict], coupon_percent: int = 0) -> int:
    subtotal = sum(item["price_cents"] * item["qty"] for item in items)
    return apply_discount(subtotal, coupon_percent)


def item_count(items: list[dict]) -> int:
    total = 0
    for item in items:
        total = total + item.get("qty")
    return total
