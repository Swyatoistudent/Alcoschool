import pytest
from Trees.binary_search_tree import BinSearchTree


@pytest.mark.parametrize('values, pre_dfs_return', [
    ([], []),
    ([1], [1]),
    ([2, 1, 5, 8, 4], [2, 1, 5, 4, 8])
])
def test_tree_dfs_pre(values, pre_dfs_return):
    l1 = BinSearchTree()

    for v in values:
        l1.add(v)
    assert l1.to_list_dfs("pre") == pre_dfs_return


@pytest.mark.parametrize('values, bfs_return', [
    ([], []),
    ([1], [1]),
    ([8, 10, 3, 14, 13, 1, 6, 4, 7], [8, 3, 10, 1, 6, 14, 4, 7, 13])
])
def test_tree_bfs(values, bfs_return):
    l1 = BinSearchTree()

    for v in values:
        l1.add(v)
    assert l1.to_list_bfs() == bfs_return
