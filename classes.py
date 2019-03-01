class pets():
    def __init__(self, name, color, species, fur):
        self.n = name
        self.s = species
        self.c = color
        self.f = fur

    def __str__(self):
        return 'name: {}, species: {}, color: {}, fur: {}'.format(self.n, self.s, self.c, self.f)

    def characteristics(self):
        return {'name':self.n, 'species':self.s, 'color':self.c, 'fur':self.f}


class Dog(pets):
    def __init__(self, name, color):
        pets.__init__(self, name, color, species='Dog', fur=True)
        self.tricks = []

    def add_tricks(self, str):
        self.tricks.append(str)


pet1 = pets(name='Tinto', species='Dog', color='Black', fur=False)
print(pet1)

pet2 = Dog(name='Fido', color='Amber')
pet2.add_tricks('sit')
pet2.add_tricks('down')

print(pet2.tricks)
properties = pet2.characteristics()
print(properties['name'])
