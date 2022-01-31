from array import array


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


class LinkedList:
    def __init__(self, initializer=None) -> None:
        """
        Initiate data object
        :param initializer: optional, iterable
        :return: None
        """
        self._data = list(initializer if initializer else [])

    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """
        self._data.insert(0, item)

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """
        self._data.append(item)

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        self._data.insert(index, item)

    def pop(self, pos=-1):
        """
        remove element from position pos and return it
        """
        try:
            return self._data.pop(pos)
        except IndexError:
            raise IndexError('LinkedList: pop index error')

    def head(self):
        """
        return head of linked list
        """
        try:
            return self._data[0]
        except IndexError:
            raise IndexError('LinkedList: is empty')

    def tail(self):
        """
        return tail of linked list
        """
        try:
            return self._data[-1]
        except IndexError:
            raise IndexError('LinkedList: is empty')

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self):
        return next(self._iterator)


def test_linkedlist() -> None:
    t_linkedlist = LinkedList([2, 3])
    assert len(t_linkedlist) == 2
    t_linkedlist.add_back(5)
    t_linkedlist.add_front(1)
    t_linkedlist.insert(4, 3)
    assert len(t_linkedlist) == 5
    assert t_linkedlist.head() == 1
    assert t_linkedlist.tail() == 5
    assert list(t_linkedlist) == [1, 2, 3, 4, 5]
    assert t_linkedlist.pop(2) == 3
    assert t_linkedlist.pop() == 5
    assert list(t_linkedlist) == [1, 2, 4]


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
