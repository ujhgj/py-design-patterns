from patterns.creational.builder import *

def test_build():
    builder = HouseBuilder() \
        .build_footing()\
        .build_walls()\
        .build_roof()\

    assert isinstance(builder.get_result(), House)
