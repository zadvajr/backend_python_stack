"""You could also declare declare a variable to be of type str or None"""
def say_hi(name: str | None = None):
    """say_hi(): accepts name or noe"""
    if name is not None:
        print(f"Hello {name}!")
    else:
        print("Hello World!")

say_hi("Daniel") # Calling with name
say_hi() # calling without name
