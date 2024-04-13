class Vehicle:
    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def calculate_depreciation(self, years):
        # Calculate depreciation based on the number of years
        pass

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, mileage, price, num_doors):
        super().__init__(make, model, year, mileage, price)
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

    # Additional car-specific methods


class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, price, towing_capacity):
        super().__init__(make, model, year, mileage, price)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return self.towing_capacity

    # Additional truck-specific methods


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, price, engine_size):
        super().__init__(make, model, year, mileage, price)
        self.engine_size = engine_size

    def get_engine_size(self):
        return self.engine_size

    # Additional motorcycle-specific methods
