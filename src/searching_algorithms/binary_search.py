""" Binary search implementation to efficiently search for a target element in a sorted list."""

def binary_search(arr: list, target: int) -> int:
    """Performs binary search on a sorted list to find the target element.

    Binary search is an efficient O(log n) algorithm that repeatedly divides the
    search space in half. It compares the target value with the middle element
    of the list and determines whether to continue searching in the left or
    right half. This process continues until the target is found or the search
    space is exhausted.

    Args:
        arr (list): A sorted list of elements.
        target (int): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    Time complexity: O(log n)

    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        # Find the middle index.
        mid = (left + right) // 2

        # If target equals the middle element, return its respective index.
        if arr[mid] == target:
            return mid

        # If the middle element is smaller than target, search right half.
        elif arr[mid] < target:
            left = mid + 1

        # If the middle element is larger than target, search left half.
        else:
            right = mid - 1

    # If the target does not exist in the list return -1.
    return -1

if __name__ == "__main__":

    # Test case 1: Target exists in the middle
    assert binary_search([10, 20, 30, 40, 50], 30) == 2

    # Test case 2: Target is the first element
    assert binary_search([5, 15, 25, 35, 45], 5) == 0

    # Test case 3: Target is the last element
    assert binary_search([3, 6, 9, 12, 15], 15) == 4

    # Test case 4: Target is in the left half
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == 2

    # Test case 5: Target is in the right half
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == 7

    # Test case 6: Target is not in the list
    assert binary_search([1, 3, 5, 7, 9], 4) == -1

    # Test case 7: Empty list
    assert binary_search([], 10) == -1

    # Test case 8: List with one element (target exists)
    assert binary_search([42], 42) == 0

    # Test case 9: List with one element (target does not exist)
    assert binary_search([42], 10) == -1

    # Test case 10: Large list (performance check)
    large_list = list(range(1000000))

    assert binary_search(large_list, 999999) == 999999
    assert binary_search(large_list, 500000) == 500000
    assert binary_search(large_list, 1000001) == -1

    print("All test cases passed!")
