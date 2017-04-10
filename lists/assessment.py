"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    # """Return a list of only the odd numbers in the input list.

    # For example::

    #     >>> all_odd([1, 2, 7, -5])
    #     [1, 7, -5]

    #     >>> all_odd([2, -6, 8])
    #     []
    # """
  odd_numbers = []
  
  for number in numbers:
    number = abs(number)
 
    if number % 2 > 0:
      odd_numbers.append(number)

    #   return odd_numbers
  if len(odd_numbers):
    return odd_numbers
  return ['the wrong thing']


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """
    for i, item in enumerate(items):
        print i, item
    #print("Nothing at all")


def foods_in_common(food_list_1, food_list_2):
    # """Find foods in common.

    # Given 2 lists of foods, return the items that are in common
    # between the two, sorted alphabetically.

    # **NOTE**: for this problem, you're welcome to use any of the
    # Python data structures you've been introduced to (not just
    # lists). Is there another that would be a good idea?

    # For example::

    #     >>> foods_in_common(
    #     ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
    #     ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
    #     ... )
    #     ['bagel', 'cake', 'cheese', 'kale']

    # The returned list should not have any duplicates::
    #     >>> foods_in_common(
    #     ...     ["cheese", "bagel", "cake", "cheese"],
    #     ...     ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
    #     ... )
    #     ['bagel', 'cake', 'cheese']

    # If there are no foods in common, return an empty list::

    #     >>> foods_in_common(
    #     ...     ["lamb", "chili", "cheese"],
    #     ...     ["cake", "ice cream"]
    #     ... )
    #     []

    # """
    
  food_list_1 = set(food_list_1)
  food_list_2 = set(food_list_2)

  return sorted(food_list_1 & food_list_2)
    #return ['the wrong thing']


def every_other_item(items):
    # """Return every other item in `items`, starting at first item.

    # For example::

    #   >>> every_other_item([1, 2, 3, 4, 5, 6])
    #   [1, 3, 5]

    #   >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
    #   ['pickle', 'juice', 'juice']

    #   >>> every_other_item(
    #   ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
    #   ... )
    #   ['you', 'are', 'good', 'at', 'code']
    # """
  new_lst = []
  
  for i, item in enumerate(items):
     if i % 2 == 0:
      new_lst.append(item)

  return new_lst
    #return ['the wrong thing']



def largest_n_items(items, n):
    # """Return the `n` largest integers in list, in ascending order.

    # You can assume that `n` will be less than the length of the list.

    # For example::

    #     >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    #     [59, 700, 6006]

    # It should work when `n` is 0::

    #     >>> largest_n_items([3, 4, 5], 0)
    #     []

    # If there are duplicates in the list, they should be counted
    # separately::

    #     >>> largest_n_items([3, 3, 3, 2, 1], 2)
    #     [3, 3]
    # """
  new_lst = []
  items = sorted(items)
  length = len(items)
  
  for x in range(0, n):
    new_lst.append(items[length-x-1])
  new_lst = sorted(new_lst)
  return new_lst
 
  #   #return ['the wrong thing']


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
