import pickle
import os

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname 

    def __repr__(self):
       return self.name + ' ' + self.lastname


database = 'data.pickle'

if os.path.isfile(database):
    with open(database, 'rb') as f:
        person = pickle.load(f)
        print(person)
else:
    print('no tengo data')
    person = Person('maria', 'chacon')
    with open(database, 'wb') as f:
        pickle.dump(person, f)
    