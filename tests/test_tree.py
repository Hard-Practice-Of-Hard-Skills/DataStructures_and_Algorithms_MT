from data_structures.tree import BinaryTree, Tree


def test_binarytree_init():
    tree = BinaryTree(1)
    assert tree.value == 1
    assert not tree.left
    assert not tree.right


def test_binarytree_count():
    tree = BinaryTree(1)
    assert tree.count_leaves() == 1


def test_binarytree_insert():
    tree = BinaryTree(10)
    tree.insert(20)
    assert tree.count_leaves() == 2
    assert tree.left.count_leaves() == 1
    assert tree.left.value == 20
    tree.insert(30)
    assert tree.count_leaves() == 3
    assert tree.left.count_leaves() == 1
    assert tree.right.count_leaves() == 1
    assert tree.right.value == 30
    tree.insert(40)
    assert tree.count_leaves() == 4
    assert tree.left.count_leaves() == 2
    assert tree.right.count_leaves() == 1
    assert tree.left.left.value == 40
    tree.insert(50)
    assert tree.count_leaves() == 5
    assert tree.left.count_leaves() == 3
    assert tree.right.count_leaves() == 1
    assert tree.left.right.value == 50
    tree.insert(60)
    assert tree.count_leaves() == 6
    assert tree.left.count_leaves() == 3
    assert tree.right.count_leaves() == 2
    assert tree.right.left.value == 60
    tree.insert(70)
    assert tree.count_leaves() == 7
    assert tree.left.count_leaves() == 3
    assert tree.right.count_leaves() == 3
    assert tree.right.right.value == 70


def test_tree_init():
    joe = Tree('Joe')
    assert str(joe) == 'Joe []'


def test_tree_add_child():
    joe = Tree('Joe')
    jan = Tree('Jan')
    dan = Tree('Dan')
    sam = Tree('Sam')
    jan.add_child(dan)
    assert str(jan) == 'Jan [Dan]'
    jan.add_child(sam)
    assert str(jan) == 'Jan [Dan, Sam]'
    joe.add_child(jan)
    assert str(joe) == 'Joe [Jan +2 children]'
    assert str(dan) == 'Dan []'
    assert str(sam) == 'Sam []'
