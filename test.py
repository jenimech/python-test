class Animal:
  def prueba():
      print('heredado')

class Person(Animal):
    city = "Montevideo"

    def __init__(self, name, lastname):
        self.__name = name
        self.__lastname = lastname

    def __str__(self):
        return 'Person(' + self.__name + ', ' + self.__lastname + ')'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def staticmethod():
      print("soy un metodo estatico")

    @classmethod
    def classmethod(cls):
        print("soy methodo de clase")
