"""
    Gets name with Age
"""
def get_name_with_age(name:str, age:int):
    """returns name with age"""
    name_with_age = name.title() + " is this old: " + str(age)
    return name_with_age
print(get_name_with_age("daniel", 37))
