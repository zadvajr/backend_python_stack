"""
    Types and Validations
    These Env vars can only handle text strings
    Any value read in python form an env var will be a string
    So any conversion or validation has to be done in code
"""
import os

path = os.getenv("PATH", "NO PATH")
print(path)
print(type(path))
