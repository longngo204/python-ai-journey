"""
Day 3 - zip, enumerate, and sorted
Goal: Learn to pair, index, and order data cleanly.
"""

# ===== Task 1 =====
def pair_names_scores(names, scores):
    """Pair names with scores into a list of tuples."""
    return list(zip(names, scores))

# ===== Task 2 =====
def index_to_dict(items):
    """Return a dict mapping index to item using enumerate."""
    return {idx: item for idx, item in enumerate(items)}

# ===== Task 3 =====
def sort_by_score(students):
    """
    Sort list of tuples (name, score) by score descending.
    Example: [("Alice", 80), ("Bob", 90)] -> [("Bob", 90), ("Alice", 80)]
    """
    return sorted(students, key=lambda x: x[1], reverse=True)

# ===== Task 4 =====
def merge_and_sort_lists(list1, list2):
    """Merge two lists and return sorted ascending list."""
    merged_list =  list1 + list2 
    return sorted(merged_list)

if __name__ == "__main__":
    print(pair_names_scores(["Alice", "Bob"], [85, 92]))
    print(index_to_dict(["apple", "banana", "kiwi"]))
    print(sort_by_score([("Alice", 80), ("Bob", 90), ("Charlie", 85)]))
    print(merge_and_sort_lists([5, 1, 3], [2, 4]))
