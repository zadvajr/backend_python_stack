"""You can as well create an env vars for specific program executions only"""
import os

user_name = os.getenv("USER_NAME", "DEFAULT USER")
print(f"Hello {user_name} form python")
