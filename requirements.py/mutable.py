def change_item(lst, index, value):
    lst[index] = value
    return lst


def add_item(lst, item):
    lst.append(item)
    return lst


def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst


def remove_item(lst, item):
    lst.remove(item)
    return lst


def pop_last(lst):
    return lst.pop()


def sort_list(lst):
    lst.sort()
    return lst


def reverse_list(lst):
    lst.reverse()
    return lst


if __name__ == "__main__":
    fruits = ["apple", "banana", "cherry"]
    print("Original:", fruits)
    change_item(fruits, 1, "mango")
    add_item(fruits, "orange")
    insert_item(fruits, 0, "grapes")
    remove_item(fruits, "apple")
    print("After changes:", fruits)
    print("Popped:", pop_last(fruits))
    print("Sorted:", sort_list(fruits))
    print("Reversed:", reverse_list(fruits))