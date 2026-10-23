"""You can declare type: union"""
def process_items(items: list[str | int]):
    """define type union"""
    return items
person = ["Daniel", 38]

print(process_items(person))
