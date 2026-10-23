"""Type Parameters: Generic type -> dict"""

def process_items(prices: dict[str, float]):
    """process item: dict"""
    for item_name, item_price in prices.items():
        print(item_name, ":", item_price)
items = {
    "Pencil": 50.00,
    "Pen": 100.00,
    "Book": 250.00
}

process_items(items)
