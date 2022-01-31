"""
Stack type implementation
"""
from typing import Any


class Stack:
    """
    Queue type implementation using list as a data storage
    :param initializer: optional, iterable
    :return: None
    """
    def __init__(self, initializer=None) -> None:
        if initializer:
            self._data = list(initializer)
        else:
            self._data = []

    def pop(self) -> Any:
        """
        return item from stack and removes it,
        None if stack is empty
        """
        if self._data:
            return self._data.pop()
        else:
            return None

    def push(self, item: Any) -> None:
        """
        add item to stack
        """
        self._data.append(item)

    def peek(self) -> Any:
        """
        return item from stack (doesn't remove it),
        None if stack is empty
        """
        if self._data:
            return self._data[-1]
        else:
            return None

    def __len__(self) -> int:
        """
        return amount of items in stack
        """
        return len(self._data)

    def __bool__(self):
        """
        return true if stack is empty
        """
        return bool(self._data)

    def __str__(self) -> str:
        """
         return string representation of the Stack
        """
        return f'Stack: {str(list(reversed(self._data)))}'


def test_stack() -> None:
    t_stack = Stack()
    assert not t_stack
    assert not t_stack.pop()
    assert not t_stack.peek()
    assert len(t_stack) == 0
    t_stack.push(100)
    assert t_stack
    assert len(t_stack) == 1
    assert t_stack.peek() == 100
    t_stack.push(200)
    assert len(t_stack) == 2
    assert t_stack.peek() == 200
    assert t_stack.pop() == 200
    assert t_stack
    assert t_stack.pop() == 100
    assert not t_stack
