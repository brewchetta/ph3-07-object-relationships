# python -i classes/neighborhood.py

class Neighborhood:
    # street, city
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __repr__(self):
        return f"Neighborhood(street={self.street}, city={self.city})"
    
    def homes(self):
        return [ home for home in Home.all_homes if home.neighborhood == self ]


class Home:

    all_homes = []

    # address
    def __init__(self, address, neighborhood):
        self.address = address
        self.neighborhood = neighborhood
        Home.all_homes.append(self)

    def __repr__(self):
        return f"Home(address={self.address}, neighborhood={self.neighborhood})"
    
    def residents(self):
        return [ res for res in Resident.all_residents if res.home == self ]
    
    @property
    def neighborhood(self):
        return self._neighborhood
    
    @neighborhood.setter
    def neighborhood(self, new_neigh):
        if isinstance(new_neigh, Neighborhood):
            self._neighborhood = new_neigh
        else:
            raise TypeError("WRONG! TURN BACK!")

# home1.residents() ===> [r1,r2,r3]

class Resident:

    all_residents = []

    # name, vehicle
    def __init__(self, name, vehicle, home):
        self.name = name
        self.vehicle = vehicle
        self.home = home
        Resident.all_residents.append(self)

    def __repr__(self):
        return f"Resident(name={self.name}, vehicle={self.vehicle})"

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, new_home):
        if isinstance(new_home, Home):
            self._home = new_home
        else:
            raise TypeError("This is not a home!")


n1 = Neighborhood("1", "Manhattan")
n2 = Neighborhood("2", "Brooklyn")

h1 = Home("123 Sesame Street", n2)
h2 = Home("11 Broadway", n1)
h3 = Home("1 World Trade Center", n1)
h4 = Home("Fulton Street", n2)

r1 = Resident("Mohammad", "Harley Davidson", h2)
r2 = Resident("Joseph", "4 Train", h3)
r3 = Resident("Aaron", "6 Train", h4)
r4 = Resident("Jaeem", "7 Train", h1)
r5 = Resident("Anton", "N Train", h3)
r6 = Resident("Chett", "4 Train", h4)



####################################################################

class Park:
    # neighborhood has many parks
    # park belongs to a neighborhood
    pass


class Visit:
    # visit belongs to a park
    # visit belongs to a resident
    # resident has many visits
    # park has many visits
    # residents have many parks through visits
    # parks have many residents through visits
    pass