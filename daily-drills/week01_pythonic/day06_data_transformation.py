"""
Day 6 - Mixed Data Transformation
Goal: Apply multiple Python tools together.
"""
from collections import Counter
import itertools
# ===== Task 1 =====
def flatten_list(nested):
    """Flatten a list of lists into a single list."""
    return [item for items in nested for item in items]

# ===== Task 2 =====
def group_by_length(words):
    """Return dict grouping words by their length."""
    return {length: [word for word in words if len(word) == length] 
                for length in set(map(len, words))}


# ===== Task 3 =====
def top_n_frequent(items, n):
    """Return top n most frequent items from list."""
    return Counter(items).most_common(n)

# ===== Task 4 =====
def running_total(nums):
    """Return list of running totals from nums."""
    return list(itertools.accumulate(nums))

if __name__ == "__main__":
    print(flatten_list([[1, 2], [3, 4], [5]]))
    print(group_by_length(["apple", "bat", "cat", "banana", "kiwi"]))
    print(top_n_frequent(["a", "b", "a", "c", "b", "a"], 2))
    print(running_total([1, 2, 3, 4]))
