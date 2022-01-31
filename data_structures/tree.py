class BinaryTree:
    class __Node:
        def __init__(self):
            self.left_leaf = None
            self.right_leaf = None

    def __init__(self):
        self.root = self.__Node()

    def draw(self):
        raise NotImplementedError()


class Tree:
    class __Node:
        def __init__(self):
            self.children = []

    def __init__(self):
        self.root = self.__Node()

    def draw(self):
        raise NotImplementedError()
