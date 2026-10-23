"""defining a variable with type parameter for tupple and set"""
from typing import Tuple, Set

def process_items(items_t: Tuple[int, int, str], item_s: Set[bytes]):
    """process items"""
    return items_t, item_s

data_a = (38, 165.5, "Daniel")
data_b = {b"Hello", b"World"}

process_items(data_a, data_b)

