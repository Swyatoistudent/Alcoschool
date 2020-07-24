import pytest
from .list import Linked_list
@pytest.mark.parametrize('values', [
        [],
        [1],
        [1,3,2]
    ])
def test_list_prepend(values):
    l1 = Linked_list()
    for v in values:
        l1.prepend(v)
    assert l1.to_list()== list(reversed(values))

@pytest.fixture
def empty_list():
    print("kkk1")
    l1 = Linked_list()
    yield l1
    print("kkk2")

@pytest.mark.parametrize('values, expected', [
    ([], []),
    ([1],[1]),
    ([1,3,2],[2,3,1])
    ])
def test_list_prepend2(values,expected,empty_list):
    l1 = empty_list
    for v in values:
        l1.prepend(v)
    assert l1.to_list()== expected

@pytest.mark.parametrize('values, expected_length', [
    ([],0),
    ([1], 1),
    ([2,3,4,5],4)
])
@pytest.mark.parametrize('print_yo',[True,False])
def test_list_len(values,expected_length,empty_list,print_yo):
    if print_yo:
        print('uo')
    l1= empty_list
    for v in values:
        l1.prepend(v)
    assert l1.len() == expected_length
