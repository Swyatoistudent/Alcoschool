import pytest
from Trees.AVL.avl import AVLTree
@pytest.mark.parametrize('values, bfs_return', [
    ([], []),
    ([1], [1]),
    ([1,2,3], [2,1,3]),
    ([8, 10, 3, 14, 13, 1, 6, 4, 7], [8, 3, 13, 1, 6, 10, 14,4, 7])
])
def test_tree_bfs(values, bfs_return):
    l1 = AVLTree()

    for v in values:
        l1.insert(v)
    assert l1.to_list_bfs() == bfs_return