"""
    Declaring simple types
"""
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    """returns simple items"""
    return item_a, item_b, item_c, item_d, item_e

print(get_items("Daniel", 37, 165.50, True, 'b'))
