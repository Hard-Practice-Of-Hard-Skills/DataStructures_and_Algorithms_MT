"""
Queue and PrioritizingQueue types implementation
"""
from typing import Any

import pytest


class Queue:
    """
    Queue type implementation using list as a data storage
    :param initializer: optional, iterable
    :param maxlength: optional, integer
    :return: None
    """

    def __init__(self, maxlength=None) -> None:
        self.maxlength = maxlength
        self._data = []

    @classmethod
    def create_from_iterable_v1(cls, iterable, max_length=None):
        instance = cls(max_length)
        for item in iterable:
            instance.put(item)
        return instance

    @classmethod
    def create_from_iterable_v2(cls, iterable, max_length=None):
        instance = cls(max_length)
        data = list(iterable)
        instance._check_capacity(len(iterable))
        instance._data = data
        return instance

    def _check_capacity(self, length):
        if self.maxlength and length > self.maxlength:
            raise BufferError('Queue: max length exceeded')

    def put(self, item) -> None:
        """
        put element to the queue
        """
        self._check_capacity(len(self) + 1)
        self._data.append(item)

    def get(self) -> Any:
        """
        get element from queue, but doesn't remove it
        """
        try:
            return self._data[0]
        except IndexError:
            raise IndexError('Queue: is empty')

    def remove(self) -> Any:
        """
        remove element from queue
        """
        try:
            return self._data.pop(0)
        except IndexError:
            raise IndexError('Queue: is empty')

    def __bool__(self) -> bool:
        """
        returns true if there is at least one element in queue
        """
        return bool(self._data)

    def __str__(self) -> str:
        """
        returns string representation of the queue
        """
        return f'<<{" ".join([str(i) for i in self._data])}<'

    def __repr__(self) -> str:
        """
        returns detailed representation of the queue object
        """
        return f'Queue object: <<{" ".join([str(i) for i in self._data])}<'

    def __len__(self) -> int:
        """
        returns length of the queue
        """
        return len(self._data)

    def __iter__(self) -> object:
        """
        returns iterator object of the queue
        """
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self) -> object:
        """
        returns next object from the queue
        """
        return next(self._iterator)


class TestQueue:
    def test_get(self):
        q = Queue()
        q._data = [1, 2, 3]

        assert q.get() == 1
        assert len(q) == 3

    def test_remove(self):
        q = Queue()
        q._data = [1, 2, 3]

        assert q.remove() == 1
        assert len(q) == 2

    def test_put(self):
        q = Queue()

        q.put(1)
        assert len(q) == 1

    def test_create_from_iterable_v1(self):
        q = Queue.create_from_iterable_v1([1, 2, 3])
        assert len(q) == 3


class TestSizedQueue:
    # can be done with mark.parametrize to not copy and paste
    def test_get(self):
        q = Queue(3)
        q._data = [1, 2, 3]

        assert q.get() == 1
        assert len(q) == 3

    # can be done with mark.parametrize to not copy and paste
    def test_put(self):
        q = Queue()

        q.put(1)
        assert len(q) == 1

    def test_put_when_max_len_exceeded(self):
        q = Queue(maxlength=1)

        q.put(1)
        with pytest.raises(BufferError):
            q.put(2)

    # can be done with mark.parametrize to not copy and paste
    def test_create_from_iterable_v1(self):
        q = Queue.create_from_iterable_v1([1, 2, 3])
        assert len(q) == 3

    def test_create_from_iterable_v1_when_max_len_exceeded(self):
        with pytest.raises(BufferError):
            Queue.create_from_iterable_v1([1, 2, 3], 2)


def test_queue() -> None:
    t_queue = Queue(maxlength=3)
    assert not t_queue
    assert t_queue.maxlength == 3
    try:
        t_queue.get()
    except IndexError:
        pass
    else:
        raise AssertionError('Test Queue: self.get() on empty queue error')
    try:
        t_queue.remove()
    except IndexError:
        pass
    else:
        raise AssertionError('Test Queue: self.remove() on empty queue error')
    t_queue.put(1)
    t_queue.put(2)
    t_queue.put(3)
    assert t_queue
    assert len(t_queue) == 3
    assert t_queue.get() == 1
    assert list(t_queue) == [1, 2, 3]
    try:
        t_queue.put(4)
    except BufferError:
        pass
    else:
        raise AssertionError('Test Queue: _check_capacity does not work')
    assert t_queue.remove() == 1
    assert t_queue.remove() == 2
    assert list(t_queue) == [3]


class PriorityQueue:
    """
    PriorityQueue type implementation using list as a data storage
    :param initializer: optional, iterable
    :param maxlength: optional, integer
    :param revers: optional Boolean
    :return: None
    """

    def __init__(self,
                 initializer=None, maxlength=None, revers=False) -> None:
        self.maxlength = maxlength
        self.revers = revers
        if initializer:
            self._check_capacity(len(initializer))
            self._data = list(initializer)
        else:
            self._data = []

    def _check_capacity(self, length) -> None:
        if self.maxlength and length > self.maxlength:
            raise BufferError('PriorityQueue: max length exceeded')

    def put(self, item) -> None:
        """
        put element to the queue
        """
        self._check_capacity(len(self) + 1)
        self._data.append(item)

    def _get_priority_value(self) -> Any:
        """
        return priority value depending on queue order
        """
        if self.revers:
            return max(self._data)
        else:
            return min(self._data)

    def get(self) -> Any:
        """
        get element from queue, but doesn't remove it
        """
        if self._data:
            return self._get_priority_value()
        else:
            raise IndexError('Queue: is empty')

    def remove(self) -> Any:
        """
        remove element from queue
        """
        if self._data:
            remove_value = self._get_priority_value()
            self._data.remove(remove_value)
            return remove_value
        else:
            raise IndexError('Queue: is empty')

    def __bool__(self) -> bool:
        """
        returns true if there is at least one element in queue
        """
        return bool(self._data)

    def __str__(self) -> str:
        """
        returns string representation of the queue
        """
        return f'<<{" ".join([str(i) for i in self._data])}<'

    def __repr__(self) -> str:
        """
        returns detailed representation of the queue object
        """
        return ('PriorityQueue object: <<'
                f'{" ".join([str(i) for i in self._data])}<')

    def __len__(self) -> int:
        """
        returns length of the queue
        """
        return len(self._data)

    def __iter__(self) -> object:
        """
        returns iterator object of the queue
        """
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self) -> object:
        """
        returns next object from the queue
        """
        return next(self._iterator)


def test_priority_queue() -> None:
    t_priorityqueue = PriorityQueue(maxlength=3)
    assert t_priorityqueue.maxlength == 3
    assert not t_priorityqueue
    try:
        t_priorityqueue.get()
    except IndexError:
        pass
    else:
        raise AssertionError(
            'Test PriorityDeque: self.get() on empty queue error')
    try:
        t_priorityqueue.remove()
    except IndexError:
        pass
    else:
        raise AssertionError(
            'Test PriorityDeque: self.remove() on empty queue error')
    t_priorityqueue.put(9)
    t_priorityqueue.put(1)
    t_priorityqueue.put(5)
    assert t_priorityqueue
    assert len(t_priorityqueue) == 3
    try:
        t_priorityqueue.put(4)
    except BufferError:
        pass
    else:
        raise AssertionError(
            'Test PriorityDeque: _check_capacity does not work')
    assert t_priorityqueue.get() == 1
    assert t_priorityqueue.remove() == 1
    assert t_priorityqueue.remove() == 5
    assert list(t_priorityqueue) == [9]
    t_priorityqueue = PriorityQueue([7, 9, 1], revers=True)
    assert t_priorityqueue.remove() == 9
    assert t_priorityqueue.remove() == 7
    assert list(t_priorityqueue) == [1]
