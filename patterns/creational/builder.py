class CarAttributes:
    def __init__(self):
        self.gps = False
        self.engine = False
        self.trip_computer = False
        self.seats = False
        self.wheels = False

class Car(CarAttributes):
    """
    A vehicle
    """
    pass

class CarManual(CarAttributes):
    """
    A documentation for a car
    """
    pass

class BuilderInterface:
    """
    Design Pattern: Builder
    """
    def set_seats(self):
        return self

    def set_engine(self):
        return self

    def set_trip_computer(self):
        return self

    def set_gps(self):
        return self

    def set_wheels(self):
        return self

    def get_result(self):
        pass

class CarBuilder(BuilderInterface):
    """
    Builder for a car
    """
    def __init__(self):
        self.car = Car()

    def set_seats(self):
        self.car.seats = True
        return self

    def set_engine(self):
        self.car.engine = True
        return self

    def set_trip_computer(self):
        self.car.trip_computer = True
        return self

    def set_gps(self):
        self.car.gps = True
        return self

    def set_wheels(self):
        self.car.wheels = True
        return self

    def get_result(self):
        return self.car

class CarManualBuilder(BuilderInterface):
    """
    """
    def __init__(self):
        self.car_manual = CarManual()

    def set_seats(self):
        self.car_manual.seats = True
        return self

    def set_engine(self):
        self.car_manual.engine = True
        return self

    def set_trip_computer(self):
        self.car_manual.trip_computer = True
        return self

    def set_gps(self):
        self.car_manual.gps = True
        return self

    def set_wheels(self):
        self.car_manual.wheels = True
        return self

    def get_result(self):
        return self.car_manual

class Director:
    """
    Design Pattern: Director
    """
    def make_van(self, builder: BuilderInterface):
        return builder\
            .set_engine()\
            .set_wheels()\
            .set_wheels()\
            .set_gps()\
            .set_trip_computer()\
            .get_result()

    def make_sports_car(self, builder: BuilderInterface):
        return builder\
            .set_wheels() \
            .set_gps() \
            .set_engine() \
            .set_wheels() \
            .set_trip_computer() \
            .get_result()
