"""You can also define class as a type"""
class Person:
    """Class Person"""
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    """Method..."""
    print(one_person.name)
person1 = Person("Daniel")
get_person_name(person1)
