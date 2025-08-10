"""
Day 1 - List & Dict Comprehensions
Goal: Practice concise, Pythonic ways to transform data.
"""

# ===== Task 1 =====
def squares_list(nums):
    """
    Given a list of integers, return a new list containing their squares.
    Example: [1, 2, 3] -> [1, 4, 9]
    """
    # TODO: implement with list comprehension
    return [n**2 for n in nums]

# ===== Task 2 =====
def tuple_list_to_dict(pairs):
    """
    Given a list of tuples (name, age), return a dict {name: age}.
    Example: [("Alice", 30), ("Bob", 25)] -> {"Alice": 30, "Bob": 25}
    """
    # TODO: implement with dict comprehension
    return {name:age for name, age in pairs}

# ===== Task 3 =====
def filter_even_numbers(nums):
    """
    Given a list of integers, return a new list containing only even numbers.
    Example: [1, 2, 3, 4] -> [2, 4]
    """
    # TODO: implement with list comprehension + filtering
    return [n for n in nums if n%2 ==0]


if __name__ == "__main__":
    print(squares_list([1, 2, 3, 4]))
    print(tuple_list_to_dict([("Alice", 30), ("Bob", 25)]))
    print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
