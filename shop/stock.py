def reserve(stock: dict, sku: str, qty: int) -> bool:
    if stock.get(sku, 0) >= qty:
        stock[sku] -= qty
        return True
    return False


def release(stock: dict, sku: str, qty: int) -> None:
    stock[sku] = stock.get(sku) + qty
