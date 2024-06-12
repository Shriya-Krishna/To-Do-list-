"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
from my_module.functions import remove_Items,edits, adding_Items, print_List

def sample_list():
    return ["item1", "item2", "item3"]

# Test for remove_items
def test_remove_items(sample_list):
    todo_list, outputs = remove_items(sample_list.copy(), [2, 0])
    assert todo_list == ["item1", "item3"]
    assert outputs == ["Item has been deleted"]

    todo_list, outputs = remove_items(sample_list.copy(), [5, 0])
    assert todo_list == ["item1", "item2", "item3"]
    assert outputs == ["That item is not in your list. Try again."]

# Test for edits
def test_edits(sample_list):
    todo_list, outputs = edits(sample_list.copy(), [(2, "newitem"), (0, "")])
    assert todo_list == ["item1", "Newitem", "item3"]
    assert outputs == ["Item 2 has been changed to newitem"]

    todo_list, outputs = edits(sample_list.copy(), [(5, "newitem"), (0, "")])
    assert todo_list == ["item1", "item2", "item3"]
    assert outputs == ["That is not a valid number. Try again."]

# Test for adding_items
def test_adding_items(sample_list):
    todo_list, outputs = adding_items(sample_list.copy(), ["item4", "done"])
    assert todo_list == ["item1", "item2", "item3", "Item4"]
    assert outputs == ["Added item4"]

    todo_list, outputs = adding_items(sample_list.copy(), ["item2", "done"])
    assert todo_list == ["item1", "item2", "item3"]
    assert outputs == ["Item2 is a duplicate and not added."]

# Test for print_list
def test_print_list(sample_list):
    output = print_list(sample_list)
    expected_output = "\n\n1: item1\n2: item2\n3: item3\n"
    assert output == expected_output