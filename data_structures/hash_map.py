import pytest
from typing import Any


def my_hash(size: int, value: Any) -> int:
    """
    Return hash for any object witch has str method
    :param size: result will be more than zero and less than size
    :param value: any object having str method
    :return: int
    """
    result = 0
    for char in str(value):
        result += ord(char)
    return result % size


class HashMapCollision:
    """
    HashMap implementation without collision handling
    :param size: int, hashmap size, by default=50
    :return: None
    """
    def __init__(self, size=5) -> None:
        self.size = size
        self.hash_map = [None] * size
        self.filled = 0

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
        hashed_key = my_hash(self.size, key)
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
        hashed_key = my_hash(self.size, key)
        if not self.hash_map[hashed_key]:
            raise KeyError
        _, value = self.hash_map[hashed_key]
        return value

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        hashed_key = my_hash(self.size, key)
        if not self.hash_map[hashed_key]:
            self.filled += 1
        if self.filled / self.size >= 0.75:
            # expand hash table if it's filled more than 75%
            self.hash_map.extend([None] * self.size)
            self.size = len(self.hash_map)
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


def test_hashmap_init(test_class=HashMapCollision):
    hm = test_class(size=2)
    assert not bool(hm)
    assert str(hm) == '[None, None]'


def test_hashmap_key_error(test_class=HashMapCollision):
    hm = test_class(size=5)
    with pytest.raises(KeyError):
        assert hm[0]


def test_hashmap_set(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[0] = 0
    assert hm[0] == 0
    assert bool(hm)
    hm[1] = 1
    assert hm[1] == 1
    hm[5] = 5
    assert hm[5] == 5


def test_hashmap_extend(test_class=HashMapCollision):
    hm = test_class(size=4)
    hm[0] = 0
    hm[1] = 1
    assert hm.size == 4
    hm[2] = 2
    assert hm.size == 8


def test_hashmap_get(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[1] = 1
    assert hm.get(1) == 1
    assert hm.get(1, 100) == 1
    assert hm.get(2) is None
    assert hm.get(2, 100) == 100


def test_hashmap_put(test_class=HashMapCollision):
    hm = test_class(size=5)
    assert hm.put(1, 1) is None
    assert hm.put(1, 2) == 1
    assert hm[1] == 2


def test_hashmap_pop(test_class=HashMapCollision):
    hm = test_class(size=5)
    assert hm.pop(1) is None
    hm[1] = 10
    assert hm.pop(1) == (1, 10)
    assert not bool(hm)


def test_hashmap_items(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.items()) == {(0, 10), (2, 20)}


def test_hashmap_keys(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.keys()) == {0, 2}


def test_hashmap_values(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.values()) == {10, 20}


def test_hashmap_iter(test_class=HashMapCollision):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm) == {0, 2}


class HashMapOpenAddressing:
    pass


class HashMapSeparateChaining:
    pass
