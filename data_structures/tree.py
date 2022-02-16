"""
Binary tree (with integers) and
general tree classes implementation
"""

from math import isqrt


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left_tree = right_tree = ''
        if self.left:
            left_tree += f'{str(self.left)} '
        if self.right:
            right_tree += f' {str(self.right)}'
        return f'{left_tree}{str(self.value)}{right_tree}'

    def count_leaves(self):
        left_leaves = right_leaves = 0
        if self.left:
            left_leaves = self.left.count_leaves()
        if self.right:
            right_leaves = self.right.count_leaves()
        return 1 + left_leaves + right_leaves

    def insert(self, data: int):
        if not self.left:
            self.left = BinaryTree(data)
        elif not self.right:
            self.right = BinaryTree(data)
        else:
            left = self.left.count_leaves() - 1
            right = self.right.count_leaves() - 1
            if left == right or left % 2:
                self.left.insert(data)
            else:
                self.right.insert(data)

    def draw_horizontal(self, level=0):
        if self.right:
            self.right.draw_horizontal(level + 1)
        print(' ' * 6 * level, self.value)
        if self.left:
            self.left.draw_horizontal(level + 1)

    def draw_vertical(self, indent=0, branch=''):
        """
        Need to do it without recursion and line breaks,
        but I'm too lazy ;)
        """
        if not indent:
            indent = (isqrt(self.count_leaves()) + 1) ** 2
        if branch == '/':
            print(' ' * (indent + 1), branch)
        elif branch == '\\':
            print(' ' * (indent - 1), branch)
        print(' ' * indent, self.value)
        if self.left:
            self.left.draw_vertical(indent // 2, '/')
        if self.right:
            self.right.draw_vertical(indent + 2, '\\')


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        children = ''
        for child in self.children:
            children += child.data
            if child.children:
                children += f' +{len(child.children)} children'
            children += ', '
        return f"{self.data} [{children.rstrip(', ')}]"

    def add_child(self, child):
        if isinstance(child, Tree):
            self.children.append(child)
        else:
            raise TypeError(f'Tree: can\'t add {type(child)} as a child')

    def draw(self, root=True, prefix='', last=True, from_last=False):
        if root:
            branch = ''
        else:
            prefix += '  ' if from_last else '│ '
            branch = '└-' if last else '├-'
        print(f'{prefix}{branch}{self.data}')
        total_children = len(self.children)
        from_last = last
        for i in range(total_children):
            child = self.children[i]
            last = i == total_children - 1
            child.draw(False, prefix, last, from_last)


def print_binary_tree():
    bin_tree = BinaryTree(1)
    for i in range(2, 9):
        bin_tree.insert(i)
    print('--------- Horizontal ----------')
    bin_tree.draw_horizontal()
    print('--------- Vertical ------------')
    bin_tree.draw_vertical()


def print_tree():
    print('----------- Tree --------------')
    root = Tree('Root')
    child1 = Tree('Child 1')
    root.add_child(child1)
    child2 = Tree('Child 2')
    root.add_child(child2)
    child3 = Tree('Child 3')
    root.add_child(child3)
    child11 = Tree('Child 1.1')
    child1.add_child(child11)
    child12 = Tree('Child 1.2')
    child1.add_child(child12)
    child121 = Tree('Child 1.2.1')
    child12.add_child(child121)
    child122 = Tree('Child 1.2.2')
    child12.add_child(child122)
    child123 = Tree('Child 1.2.3')
    child12.add_child(child123)
    child13 = Tree('Child 1.3')
    child1.add_child(child13)
    child131 = Tree('Child 1.3.1')
    child13.add_child(child131)
    child1311 = Tree('Child 1.3.1.1')
    child131.add_child(child1311)
    child1312 = Tree('Child 1.3.1.2')
    child131.add_child(child1312)
    child31 = Tree('Child 3.1')
    child3.add_child(child31)
    child311 = Tree('Child 3.1.1')
    child31.add_child(child311)
    child32 = Tree('Child 3.2')
    child3.add_child(child32)
    print(root)
    root.draw()
    print('-' * 30)
    print(child1)
    child1.draw()
    print('-' * 30)
    print(child2)
    child2.draw()
    print('-' * 30)
    print(child3)
    child3.draw()


if __name__ == '__main__':
    print_binary_tree()
    print_tree()
