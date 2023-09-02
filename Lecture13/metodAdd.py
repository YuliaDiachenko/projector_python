class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other):
        return Country(self.name+" "+other.name, self.population+other.population)

    def __add__(self, other):
        return Country(self.name+" "+other.name, self.population+other.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

#____1____________
#bosnia_herzegovina = bosnia.add(herzegovina)

#____2____________
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)