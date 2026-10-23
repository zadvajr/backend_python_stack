"""Adding metadata to type hints"""
from typing import Annotated

def say_hi(name: Annotated[str, "Additional metadata goes here"]) -> str:
    """say_hi()"""
    return f"Hello, {name}"

print(say_hi("Daniel"))
