from patterns.creational.singleton import *

def test_instantiation1():
    instance_1 = Singleton()
    instance_2 = Singleton()
    assert id(instance_1) == id(instance_2)

def test_instantiation2():
    db_1 = Database()
    db_2 = Database()
    assert id(db_1) == id(db_2)
