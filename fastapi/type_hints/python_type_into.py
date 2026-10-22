"""
    Python Types Intro: Motivation
"""
def get_full_name(first_name, last_name):
    """
        Returns full name given first and last name
    """
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe")) # Prints John Doe
