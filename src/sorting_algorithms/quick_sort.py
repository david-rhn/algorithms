""" Quick sort implementation to efficiently sort an unordered list in asccending order."""

def quick_sort(arr: list) -> list:
    """ Sorts an array using the QuickSort algorithm.

    QuickSort is a divide-and-conquer sorting algorithm that:
    1. Selects an anchor element.
    2. Partitions the array into elements less than, equal to, and greater than the anchor.
    3. Recursively sorts the left and right sub-arrays.

    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        (list): A new sorted list containing the elements of the input list in ascending order.

    Time complexity:
    - Best & Average Case: O(n log n)
    - Worst Case: O(n²) (when the anchor is always the smallest or largest element)
    """

    # If the array contains one or zero elements its already sorted.
    if len(arr) <= 1:
        return arr

    # Choosing middle element as pivot.
    anchor = arr[len(arr) // 2]

    # Elements smaller than anchor.
    left = [x for x in arr if x < anchor]

    # Element(s) that equal anchor.
    middle = [x for x in arr if x == anchor]

    # Elements greater than anchor.
    right = [x for x in arr if x > anchor]

    # Recursive sort.
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Test Case 1: Normal list
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

    # Test Case 2: Already sorted list
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test Case 3: Reverse sorted list
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test Case 4: List with duplicate values
    assert quick_sort([4, 2, 4, 3, 1, 2]) == [1, 2, 2, 3, 4, 4]

    # Test Case 5: List with all identical values
    assert quick_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]

    # Test Case 6: Single element list
    assert quick_sort([42]) == [42]

    # Test Case 7: Empty list
    assert quick_sort([]) == []

    # Test Case 8: List with negative numbers
    assert quick_sort([-3, -1, -4, -2, 0, 2, 1]) == [-4, -3, -2, -1, 0, 1, 2]

    print("All test cases passed!")