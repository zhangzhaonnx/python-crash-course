class Restuarant():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restuarant(self):
        print("There is a " + self.type +
              " Restuarant with name " + self.name.title())

    def open_restuarant(self):
        print("Restuarant " + self.name.title() + " is open")

restaurant = Restuarant("huatianjia", "Japanese")
restaurant.describe_restuarant()
restaurant.open_restuarant()