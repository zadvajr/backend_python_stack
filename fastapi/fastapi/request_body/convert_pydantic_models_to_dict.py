from pydantic import BaseModel


class User(BaseModel):
  name: str
  age: int
  email: str = "N/A"


user = User(name="Alice", age=30)

# Convert to a standard Python dictionary
data = user.model_dump()
print(data)
# Output: {'name': 'Alice', 'age': 30, 'email': 'N/A'}

# Exclude fields with default values
data_no_defaults = user.model_dump(exclude_defaults=True)
print(data_no_defaults)
# Output: {'name': 'Alice', 'age': 30}
