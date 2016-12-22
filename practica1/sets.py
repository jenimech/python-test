class Set:
    def __init__(self, arg=[]):
        self.list = arg

    def add_element(self, element):
        self.list.append(element)

    def remove_element(self, element):
        self.list.remove(element)

    @classmethod
    def diff(clr, a, b): #difference
        print([x for x in a.list if x not in b.list] + [x for x in b.list if x not in a.list])
    
    @classmethod
    def inter(clr, a, b):  #intersection
        print(list(set([x for x in a.list if x in b.list] + [x for x in b.list if x in a.list])))

