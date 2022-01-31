from array import array
from typing import Any


class ArrayList:
    """
    use 'array' module to create array data structure
    this list works only with items with the same type
    """

    def __init__(self, typecode: str, initializer=None) -> None:
        """
        Initiate data object
        :param typecode: b|B|u|h|H|i|I|j|L|q|Q|f|d
        :param initializer: optional, iterable
        :return: None
        """
        self._data = array(typecode, initializer if initializer else [])
        self._typecode = typecode

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        try:
            item_arr = array(self._typecode, [item])
        except TypeError:
            raise TypeError('ArrayList: Item insertion type error')
        new_array = self._data[:index] + item_arr + self._data[index:]
        self._data = new_array

    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """
        self.insert(item, 0)

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """
        self.insert(item, -1)

    def pop(self, pos=-1):
        """
        remove element from position pos and return it
        """
        try:
            item = self._data[pos]
        except IndexError:
            raise IndexError('ArrayList: pop index error')
        if pos == -1:
            self._data = self._data[:-1]
        else:
            self._data = self._data[:pos] + self._data[pos + 1:]
        return item

    def head(self):
        """
        return head of linked list
        """
        try:
            return self._data[0]
        except IndexError:
            raise IndexError('ArrayList: is empty')

    def tail(self):
        """
        return tail of linked list
        """
        try:
            return self._data[-1]
        except IndexError:
            raise IndexError('ArrayList: is empty')

    def __len__(self):
        return self._data.buffer_info()[1]

    def __iter__(self):
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self):
        return next(self._iterator)


def test_arraylist() -> None:
    # Question: do I need to make separate test function to each method?
    t_arraylist = ArrayList('i')
    assert len(t_arraylist) == 0
    t_arraylist.add_back(3)
    t_arraylist.add_front(1)
    t_arraylist.insert(2, 1)
    assert len(t_arraylist) == 3
    assert t_arraylist.head() == 1
    assert t_arraylist.tail() == 3
    assert list(t_arraylist) == [1, 2, 3]
    assert t_arraylist.pop(0) == 1
    assert t_arraylist.pop() == 3
    assert len(t_arraylist) == 1
    assert t_arraylist.head() == 2
    assert list(t_arraylist) == [2]


class LinkedListItem:
    """
    Item of the linked list, contains data and link to the next
    element of the list
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.link = None  # Link to the next LinkedListItem


class LinkedList:
    def __init__(self) -> None:
        """
        Initiate linked list
        :return: None
        """
        self._head = None
        self._length = 0

    def _last_item(self):
        """
        Return pointer to the last item of the list
        """
        pointer = self._head
        while pointer.link:
            pointer = pointer.link
        return pointer

    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """
        new_head = LinkedListItem(item)
        new_head.link = self._head
        self._head = new_head
        self._length += 1

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """
        new_tail = LinkedListItem(item)
        if self._head:
            pointer = self._last_item()
            pointer.link = new_tail
        else:
            self._head = new_tail
        self._length += 1

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        if self._length < index < 0:
            raise IndexError('LinkedList: insert index error')
        new_item = LinkedListItem(item)
        if self._head:
            pointer = self._head
            for _ in range(index - 1):
                pointer = pointer.link
            new_item.link = pointer.link
            pointer.link = new_item
        else:
            self._head = new_item
        self._length += 1

    def head(self):
        """
        return head of linked list
        """
        if not self._head:
            raise IndexError('LinkedList: is empty')
        return self._head.data

    def tail(self):
        """
        return tail of linked list
        """
        if not self._head:
            raise IndexError('LinkedList: is empty')
        return self._last_item().data

    def __len__(self):
        return self._length

    def __iter__(self):
        self._index = self._head
        return self

    def __next__(self):
        if self._index:
            data = self._index.data
            self._index = self._index.link
            return data
        else:
            raise StopIteration


def test_linkedlist_init() -> None:
    t_linkedlist = LinkedList()
    assert len(t_linkedlist) == 0
    assert list(t_linkedlist) == []


def test_linkedlist_head() -> None:
    t_linkedlist = LinkedList()
    t_linkedlist.add_front(1)
    assert t_linkedlist.head() == 1
    assert len(t_linkedlist) == 1
    t_linkedlist.add_front(2)
    assert t_linkedlist.head() == 2
    assert len(t_linkedlist) == 2
    assert list(t_linkedlist) == [2, 1]


def test_linkedlist_tail() -> None:
    t_linkedlist = LinkedList()
    t_linkedlist.add_back(1)
    assert len(t_linkedlist) == 1
    assert t_linkedlist.tail() == 1
    t_linkedlist.add_back(2)
    assert len(t_linkedlist) == 2
    assert t_linkedlist.tail() == 2
    assert list(t_linkedlist) == [1, 2]


def test_linkedlist_insert() -> None:
    t_linkedlist = LinkedList()
    t_linkedlist.insert('1', 0)
    assert len(t_linkedlist) == 1
    assert t_linkedlist.head() == '1'
    t_linkedlist.insert('3', 1)
    assert len(t_linkedlist) == 2
    assert t_linkedlist.tail() == '3'
    t_linkedlist.insert('2', 1)
    assert len(t_linkedlist) == 3
    assert list(t_linkedlist) == ['1', '2', '3']


class Deque:
    def __init__(self, initializer=None, maxlength=None) -> None:
        """
        Initiate data and iterator objects
        :param initializer: optional, iterable
        :param maxlength: optional, integer
        :return: None
        """
        self.maxlength = maxlength
        self._check_capacity(len(initializer))
        self._data = list(initializer if initializer else [])

    def _check_capacity(self, length):
        if self.maxlength and length > self.maxlength:
            raise BufferError('Deque: max length exceeded')

    def add_front(self, item):
        """
        add item to front of the deque (create new head)
        """
        self._check_capacity(len(self) + 1)
        self._data.insert(0, item)

    def add_back(self, item):
        """
        add item to back of the deque (create new tail)
        """
        self._check_capacity(len(self) + 1)
        self._data.append(item)

    def pop_front(self):
        """
        remove head item from the deque and return it
        """
        try:
            return self._data.pop(0)
        except IndexError:
            raise IndexError('Deque: is empty')

    def pop_back(self):
        """
        remove tail item from the deque and return it
        """
        try:
            return self._data.pop()
        except IndexError:
            raise IndexError('Deque: is empty')

    def head(self):
        """
        return head of the deque
        """
        try:
            return self._data[0]
        except IndexError:
            raise IndexError('Deque: is empty')

    def tail(self):
        """
        return tail of the deque
        """
        try:
            return self._data[-1]
        except IndexError:
            raise IndexError('Deque: is empty')

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self):
        return next(self._iterator)


def test_deque() -> None:
    t_deque = Deque(initializer=[2, 3], maxlength=5)
    assert len(t_deque) == 2
    assert t_deque.maxlength == 5
    t_deque.add_back(4)
    t_deque.add_front(1)
    assert len(t_deque) == 4
    assert t_deque.head() == 1
    assert t_deque.tail() == 4
    t_deque.add_back(5)
    try:
        t_deque.add_back(6)
    except BufferError:
        pass
    else:
        raise AssertionError('Test Deque: _check_capacity does not work')
    assert list(t_deque) == [1, 2, 3, 4, 5]
    assert t_deque.pop_front() == 1
    assert t_deque.pop_back() == 5
    assert list(t_deque) == [2, 3, 4]
