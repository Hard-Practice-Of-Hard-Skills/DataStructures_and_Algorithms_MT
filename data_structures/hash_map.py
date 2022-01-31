import pytest


class HashMap:
    """
    HashMap implementation without collision handling
    :param size: int, hashmap size, by default=50
    :return: None
    """
    def __init__(self, size=5) -> None:
        self.size = size
        self.hash_map = [None] * size

    def my_hash(self, value) -> int:
        result = 0
        for char in str(value):
            result += ord(char)
        return result % self.size

    def get(self, key, default=None):
        """
        return value for the provided key,
        return 'default' if there is no value for key
        """
        try:
            value = self[key]
        except KeyError:
            value = default
        return value

    def put(self, key, item):
        """
        set value for the provided key
        returns value of the previous value if exists, None otherwise
        """
        value = self.get(key)
        self[key] = item
        return value

    def pop(self, key):
        """
        return element for the provided key and pops it from the map
        """
        hashed_key = self.my_hash(key)
        element = self.hash_map[hashed_key]
        self.hash_map[hashed_key] = None
        return element

    def __bool__(self):
        """
        return true if map isn't empty, False otherwise
        """
        return any(self.hash_map)

    def items(self):
        """
        return sequence of (key,value) tuples
        """
        return [(item[0], item[1]) for item in self.hash_map if item]

    def keys(self):
        """
        return sequence of map keys
        """
        return [item[0] for item in self.hash_map if item]

    def values(self):
        """
        return sequence of map values
        """
        return [item[1] for item in self.hash_map if item]

    def __getitem__(self, key):
        """
        return value for the provided key,
        raise KeyError if there is no value for key
        """
        hashed_key = self.my_hash(key)
        if not self.hash_map[hashed_key]:
            raise KeyError
        _, value = self.hash_map[hashed_key]
        return value

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        hashed_key = self.my_hash(key)
        self.hash_map[hashed_key] = (key, value)

    def __iter__(self):
        # self._index = 0
        # return self
        self._iterator = iter(self.keys())
        return self._iterator

    def __next__(self):
        # while True:
        #     if self._index == self.size:
        #         raise StopIteration
        #     if self.hash_map[self._index]:
        #         break
        #     self._index += 1
        # key, _ = self.hash_map[self._index]
        # self._index += 1
        # return key
        return next(self._iterator)

    def __str__(self):
        return str(self.hash_map)


def test_hashmap_init():
    hm = HashMap(size=2)
    assert not bool(hm)
    assert str(hm) == '[None, None]'


@pytest.mark.xfail(raises=KeyError)
def test_hashmap__get():
    hm = HashMap(size=5)
    assert hm[0]


def test_hashmap_set__get():
    hm = HashMap(size=5)
    hm[0] = 0
    assert hm[0] == 0
    assert bool(hm)
    hm[1] = 1
    assert hm[1] == 1
    hm[5] = 5
    assert hm[5] == 5


def test_hashmap_get():
    hm = HashMap(size=5)
    hm[1] = 1
    assert hm.get(1) == 1
    assert hm.get(1, 100) == 1
    assert hm.get(2) is None
    assert hm.get(2, 100) == 100


def test_hashmap_put():
    hm = HashMap(size=5)
    assert hm.put(1, 1) is None
    assert hm.put(1, 2) == 1
    assert hm[1] == 2


def test_hashmap_pop():
    hm = HashMap(size=5)
    assert hm.pop(1) is None
    hm[1] = 10
    assert hm.pop(1) == (1, 10)
    assert not bool(hm)


def test_hashmap_items():
    hm = HashMap(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.items()) == {(0, 10), (2, 20)}


def test_hashmap_keys():
    hm = HashMap(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.keys()) == {0, 2}


def test_hashmap_values():
    hm = HashMap(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.values()) == {10, 20}


def test_hashmap_iter():
    hm = HashMap(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm) == {0, 2}


class HashMapOpenAddressing(HashMap):
    pass


class HashMapSeparateChaining(HashMap):
    pass
