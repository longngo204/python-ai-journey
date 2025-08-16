"""
Day 5 - Intro to NumPy
Goal: Perform basic array operations.
"""

import numpy as np

# ===== Task 1 =====
def create_random_array(n):
    """Return 1D NumPy array of n random integers between 0 and 10."""
    return np.random.randint(0,10,n)

# ===== Task 2 =====
def array_statistics(arr):
    """Return mean, median, and std of array."""
    return np.mean(arr), np.median(arr), np.std(arr)

# ===== Task 3 =====
def normalize_array(arr):
    """Return normalized array (subtract mean, divide by std)."""
    return (arr-np.mean(arr))/np.std(arr)

# ===== Task 4 =====
def elementwise_operations(a, b):
    """Return sum, difference, product of arrays a and b."""
    return a+b, a-b, a*b

if __name__ == "__main__":
    arr = create_random_array(5)
    print(arr)
    print(array_statistics(arr))
    print(normalize_array(arr))
    print(elementwise_operations(np.array([1,2,3]), np.array([4,5,6])))
