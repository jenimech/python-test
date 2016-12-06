class Set:
    def __init__(self, arg=[]):
        self.list = arg

    def add_element(self, element):
        self.list.append(element)

    def remove_element(self, element):
        self.list.remove(element)