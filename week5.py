class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

    def power_on(self):
        return f"{self.model} is now powered on."

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.gpu} GPU"

phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Adreno 740")

print(phone1.info())
print(phone1.power_on())
print(phone2.info())
print(phone2.power_on())


class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())
