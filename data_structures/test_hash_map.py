import pytest

from hash_map import (
    HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining
)


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_init(test_class):
    hm = test_class(size=2)
    assert not bool(hm)
    assert str(hm) == '[None, None]' or str(hm) == '[[], []]'


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_key_error(test_class):
    hm = test_class(size=5)
    with pytest.raises(KeyError):
        assert hm[0]


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_set(test_class):
    hm = test_class(size=5)
    hm[0] = 0
    assert hm[0] == 0
    assert bool(hm)
    hm[1] = 1
    assert hm[1] == 1
    hm[5] = 5
    assert hm[5] == 5


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_extend(test_class):
    size = 5
    hm = test_class(size=size)
    hm[0], hm[1], hm[2] = 0, 1, 2
    assert hm.size == size
    hm[3] = 3
    assert hm.size == size * 2
    assert hm[0] == 0
    assert hm[2] == 2
    hm[3], hm[4], hm[5], hm[6], hm[7], hm[8], hm[9] = 3, 4, 5, 6, 7, 8, 9
    assert hm.size == size * 2 * 2
    assert hm[0] == 0
    assert hm[2] == 2
    assert hm[6] == 6


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_get(test_class):
    hm = test_class(size=5)
    hm[1] = 1
    assert hm.get(1) == 1
    assert hm.get(1, 100) == 1
    assert hm.get(2) is None
    assert hm.get(2, 100) == 100


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_put(test_class):
    hm = test_class(size=5)
    assert hm.put(1, 1) is None
    assert hm[1] == 1
    assert hm.put(1, 2) == 1
    assert hm[1] == 2


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_pop(test_class):
    hm = test_class(size=5)
    value = hm.pop(1)
    assert value is None
    hm[1] = 10
    assert hm.pop(1) == (1, 10)
    assert not bool(hm)


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_items(test_class):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.items()) == {(0, 10), (2, 20)}


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_keys(test_class):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.keys()) == {0, 2}


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_values(test_class):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm.values()) == {10, 20}


@pytest.mark.parametrize(
    "test_class",
    [HashMapCollision, HashMapOpenAddressing, HashMapSeparateChaining]
)
def test_hashmap_iter(test_class):
    hm = test_class(size=5)
    hm[0] = 10
    hm[2] = 20
    assert set(hm) == {0, 2}
