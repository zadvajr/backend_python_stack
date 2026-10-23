"""
    Defining a list of str
"""
def process_items(items: list[str]):
    """prints items in a list of strings"""
    for item in items:
        print(item.upper())

fruits = ["Apple", "Banana", "Cherry"]

process_items(fruits)
