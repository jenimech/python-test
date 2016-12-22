class Matris:
    def __init__(self, arg=[]):
        self.list = arg

    def add_element(self, element):
        if element not in self.list:
            self.list.append(element)

    def remove_element(self, element):
        self.list.remove(element)

    @classmethod
    def diff(clr, a, b): #difference
        print([x for x in a.list if x not in b.list] + [x for x in b.list if x not in a.list])
    
    @classmethod
    def inter(clr, a, b):  #intersection
        print(list(set([x for x in a.list if x in b.list] + [x for x in b.list if x in a.list])))

    def include_set(self, b):  #include
        result = True
        for x in b.list:
            if x not in self.list:
                result = False
        print(result)

    @classmethod
    def difference_simetric(clr, a, b): #diferencia simetrica entre 2 sets
        result = Matris([x for x in a.list if x not in b.list] + [x for x in b.list if x not in a.list])
        return result

    @classmethod
    def product_cart(clr, a, b): #producto cartesiano entre 2 sets
        result = Matris([(x, y) for x in a.list for y in b.list])
        return result


