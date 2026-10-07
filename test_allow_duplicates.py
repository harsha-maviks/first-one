from ordered_list import OrderedList

def test_allow_duplicates():
    collection = OrderedList()

    collection.add(5)
    collection.add("a")
    collection.add(5)

    assert collection.get(0) == 5
    assert collection.get(1) == "a"
    assert collection.get(2) == 5
    