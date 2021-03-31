from patterns.creational.builder import *

def test_builder():
    car_builder = CarBuilder()\
        .set_engine()\
        .set_wheels()\

    assert isinstance(car_builder, CarBuilder)
    assert isinstance(car_builder.get_result(), Car)

def test_director():
    director = Director()
    sports_car = director.make_sports_car(CarBuilder())
    sports_car_manual = director.make_sports_car(CarManualBuilder())

    assert isinstance(sports_car, Car)
    assert isinstance(sports_car_manual, CarManual)
