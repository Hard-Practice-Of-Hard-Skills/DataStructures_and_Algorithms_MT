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
    :param size: int, hashmap size, by default=5
    :return: None
    """
    def __init__(self, size=5) -> None:
        self.size = size
        self.hash_map = [None] * size
        self.filled = 0
        self._index = 0

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
        index = my_hash(self.size, key)
        element = self.hash_map[index]
        self.hash_map[index] = None
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
        item = self.hash_map[my_hash(self.size, key)]
        if not item:
            raise KeyError
        return item[1]

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        index = my_hash(self.size, key)
        if not self.hash_map[index]:
            self.filled += 1
        if self.filled >= 0.75 * self.size:
            # expand hash table if it's filled more than 75%
            items = self.items()
            items.append((key, value))
            self.size *= 2
            self.hash_map = [None] * self.size
            for k, v in items:
                self.hash_map[my_hash(self.size, k)] = (k, v)
        else:
            self.hash_map[index] = (key, value)

    def __iter__(self):
        return iter(self.keys())

    def __next__(self):
        while True:
            if self._index == self.size:
                raise StopIteration
            if self.hash_map[self._index]:
                break
            self._index += 1
        key = self.hash_map[self._index][0]
        self._index += 1
        return key

    def __str__(self):
        return str(self.hash_map)


class HashMapOpenAddressing(HashMapCollision):
    """
    HashMap implementation with open addressing
    :param size: int, hashmap size, by default=5
    :return: None
    """
    def __init__(self, size=5) -> None:
        super().__init__(size)

    def __getitem__(self, key) -> Any:
        """
        return value for the provided key,
        raise KeyError if there is no value for key
        """
        index = my_hash(self.size, key)
        if not self.hash_map[index]:
            raise KeyError
        pointer = index
        while self.hash_map[pointer][0] != key:
            pointer += 1
            if pointer == index:
                raise KeyError
            if pointer == len(self.hash_map) - 1:
                pointer = 0
        return self.hash_map[pointer][1]

    def _add_to_hash_table(self, key, value) -> None:
        index = my_hash(self.size, key)
        while self.hash_map[index] and self.hash_map[index][0] != key:
            index += 1
            if index == len(self.hash_map) - 1:
                index = 0
        self.hash_map[index] = (key, value)

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        self.filled += 1
        if self.filled >= 0.75 * self.size:
            items = self.items()
            items.append((key, value))
            self.size *= 2
            self.hash_map = [None] * self.size
            for k, v in items:
                self._add_to_hash_table(k, v)
        else:
            self._add_to_hash_table(key, value)


class HashMapSeparateChaining(HashMapCollision):
    """
    HashMap implementation with Separate chaining
    :param size: int, hashmap size, by default=5
    :return: None
    """
    def __init__(self, size=5) -> None:
        super().__init__(size)
        self.hash_map = [[] for _ in range(self.size)]

    def _add_to_chain(self, key, value) -> None:
        index = my_hash(self.size, key)
        chain = self.hash_map[index]
        if chain:
            item_to_replace = None
            for k, v in chain:
                if k == key:
                    item_to_replace = (k, v)
                    break
            if item_to_replace:
                chain.remove(item_to_replace)
        chain.append((key, value))

    def __setitem__(self, key, value):
        """
        set value for the provided key
        """
        if not self.hash_map[my_hash(self.size, key)]:
            self.filled += 1
        if self.filled >= 0.75 * self.size:
            items = self.items()
            items.append((key, value))
            self.size *= 2
            self.hash_map = [[] for _ in range(self.size)]
            for k, v in items:
                self._add_to_chain(k, v)
        else:
            self._add_to_chain(key, value)

    def __getitem__(self, key) -> Any:
        """
        return value for the provided key,
        raise KeyError if there is no value for key
        """
        chain = self.hash_map[my_hash(self.size, key)]
        for k, v in chain:
            if k == key:
                return v
        raise KeyError

    def pop(self, key) -> tuple | None:
        """
        return element for the provided key and pops it from the map
        """
        found_item = None
        chain = self.hash_map[my_hash(self.size, key)]
        for k, v in chain:
            if k == key:
                found_item = (k, v)
                break
        if found_item:
            chain.remove(found_item)
        return found_item

    def items(self) -> list:
        """
        return sequence of (key,value) tuples
        """
        items = []
        for chain in self.hash_map:
            for item in chain:
                items.append(item)
        return items

    def keys(self) -> list:
        """
        return sequence of map keys
        """
        keys = []
        for chain in self.hash_map:
            for item in chain:
                keys.append(item[0])
        return keys

    def values(self) -> list:
        """
        return sequence of map values
        """
        values = []
        for chain in self.hash_map:
            for item in chain:
                values.append(item[1])
        return values


if __name__ == '__main__':
    hm = HashMapSeparateChaining()
    hm.put(1, 1)
    print(hm)
    hm.put(6, 6)
    print(hm)
