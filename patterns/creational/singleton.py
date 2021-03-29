class Singleton:
    """
    Implementation for singleton pattern
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


class Database(Singleton):
    """
    An example usage of singleton pattern
    """
