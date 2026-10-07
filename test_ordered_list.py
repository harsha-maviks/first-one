from ordered_list import OrderedList
def test_support_multiple_datatypes():
    collection = OrderedList()

    collection.add(10)
    collection.add("hello")
    collection.add(3.14)
    collection.add(True)

    assert collection.get(0) == 10
    assert collection.get(1) == "hello"
    assert collection.get(2) == 3.14
    assert collection.get(3) is True