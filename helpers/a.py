__all__ = ['MAX_PERSON', 'Person', 'even_numbers']

MAX_PERSON = 100

def even_numbers(*a):
    return [x for x in a if x % 2 == 0]

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname