from test_my_list import MyList

def test_add_end():
    """Requirement 3: back insertion"""
    my_list = MyList()
    my_list.add_end(1)
    my_list.add_end("two")
    assert my_list.get(0) == 1
    assert my_list.get(1) == "two"


def test_add_front():
    """Requirement 3: front insertion"""
    my_list = MyList()
    my_list.add_end(2)
    my_list.add_front(1)
    my_list.add_front(0.5)
    assert my_list.get(0) == 0.5
    assert my_list.get(1) == 1
    assert my_list.get(2) == 2


def test_add_in_between():
    """Requirement 3: insertion in the middle"""
    my_list = MyList()
    my_list.add_end(1)
    my_list.add_end(3)
    my_list.add_at(1, 2)
    assert [my_list.get(i) for i in range(len(my_list))] == [1, 2, 3]


def test_add_at_invalid_index():
    """Requirement 3: index out of range"""
    my_list = MyList()
    try:
        my_list.add_at(5, "x")
        assert False, "IndexError expected"
    except IndexError:
        pass


if __name__ == "__main__":
    test_add_end()
    test_add_front()
    test_add_in_between()
    test_add_at_invalid_index()
    print("Requirement 3 passed successfully")