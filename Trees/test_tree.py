import pytest
from Trees.binary_search_tree import BinSearchTree


@pytest.mark.parametrize('values, pre_dfs_return', [
    ([], []),
    ([1], [1]),
    ([2, 1, 5, 8, 4], [2, 1, 5, 4, 8])
])
def test_tree_add(values, pre_dfs_return):
    l1 = BinSearchTree()

    for v in values:
        l1.add(v)
    assert l1.to_list() == pre_dfs_return


