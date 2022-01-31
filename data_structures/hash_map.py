class HashMap:
    def get(self, key, default=None):
        """
        return value for the provided key,
        return 'default' if there is no value for key
        """
        raise NotImplementedError()

    def put(self, key, item):
        """
        set value for the provided key
        returns value of the previous value if exists, None otherwise
        """
        raise NotImplementedError()

    def pop(self, key):
        """
        return element for the provided key and pops it from the map
        """
        raise NotImplementedError()

    def __bool__(self):
        """
        return true if map isn't empty, False otherwise
        """
        raise NotImplementedError()

    def items(self):
        """
        return sequence of (key,value) tuples
        """
        raise NotImplementedError()

    def keys(self):
        """
        return sequence of map values
        """
        raise NotImplementedError()

    def values(self):
        """
        return sequence of map values
        """
        raise NotImplementedError()

    def __getitem__(self, key):
        """
        return value for the provided key,
        raise KeyError if there is no value for key
        """
        raise NotImplementedError()

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()


class HashMapOpenAddressing(HashMap):
    pass


class HashMapSeparateChaining(HashMap):
    pass
