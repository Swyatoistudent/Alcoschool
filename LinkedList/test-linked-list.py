import pytest
from LinkedList.list import Linked_list


@pytest.mark.parametrize('values', [
    [],
    [1],
    [1, 3, 2]
])
def test_list_prepend(values):
    l1 = Linked_list()
    for v in values:
        l1.prepend(v)
    assert l1.to_list() == list(reversed(values))


@pytest.fixture
def empty_list():
    l1 = Linked_list()
    yield l1


@pytest.mark.parametrize('values, expected', [
    ([], []),
    ([1], [1]),
    ([1, 3, 2], [2, 3, 1])
])
def test_list_prepend2(values, expected, empty_list):
    l1 = empty_list
    for v in values:
        l1.prepend(v)
    assert l1.to_list() == expected


@pytest.mark.parametrize('values', [
    [],
    [1],
    [2, 3, 4, 5]
])
def test_list_len_prepend(values,empty_list):
    expected_length = 0
    l1 = empty_list
    for v in values:
        l1.prepend(v)
        expected_length += 1
    assert l1.len() == expected_length


@pytest.mark.parametrize('values', [
    [],
    [1],
    [2, 3, 4, 5]
])
def test_list_len_append(values,empty_list):
    l1 = empty_list
    expected_length = 0
    for v in values:
        l1.append(v)
        expected_length += 1
    assert l1.len() == expected_length
