

import pytest
from sequence_list import orderedSequence


def test_support_multiple_datatypes():
    collection = orderedSequence()
    collection.add(10)
    collection.add("hello")
    collection.add(3.14)
    collection.add(True)
    assert collection.get(0) == 10
    assert collection.get(1) == "hello"
    assert collection.get(2) == 3.14
    assert collection.get(3) is True


def test_append_and_prepend():
    collection = orderedSequence()
    collection.add(10)
    collection.append("hello")
    collection.prepend(3.14)
    collection.prepend(True)
    assert collection.get(0) is True
    assert collection.get(1) == 3.14
    assert collection.get(2) == 10
    assert collection.get(3) == "hello"
    assert len(collection) == 4


def test_mutable_change_item():
    s = orderedSequence()
    s.add(10)
    s.add("hello")
    s.set_at(1, 3.14)
    assert s.get(1) == 3.14
    


def test_mutable_keeps_length_and_order():
    s = orderedSequence()
    for x in [1, 2, 3]:
        s.add(x)
    s.set_at(0, "a")
    assert len(s) == 3
    assert [s.get(0), s.get(1), s.get(2)] == ["a", 2, 3]


def test_mutable_invalid_index_raises():
    s = orderedSequence()
    with pytest.raises(IndexError):
        s.set_at(5, "x")
