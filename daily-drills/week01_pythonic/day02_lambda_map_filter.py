"""
Day 2 - Lambda, Map & Filter
Goal: Learn to process data using functional programming tools.
"""

# ===== Task 1 =====
def double_numbers(nums):
    """Return list where each number is doubled using map + lambda."""
    return list(map(lambda x: x*2, nums))

# ===== Task 2 =====
def filter_vowels(words):
    """Return only words starting with a vowel using filter + lambda."""
    return list(filter(lambda x: x[0].lower() in 'aeiou', words))

# ===== Task 3 =====
def normalize_names(names):
    """Convert list of names to lowercase and strip whitespace."""
    return list(map(lambda x: x.strip().lower(), names))

# ===== Task 4 =====
def fahrenheit_to_celsius(temps):
    """Convert list of temps from Fahrenheit to Celsius."""
    return list(map(lambda f: (f-32) * 5/9, temps))

if __name__ == "__main__":
    print(double_numbers([1, 2, 3, 4]))
    print(filter_vowels(["apple", "banana", "orange", "pear"]))
    print(normalize_names([" Alice ", "BOB", " Charlie "]))
    print(fahrenheit_to_celsius([32, 68, 100]))
