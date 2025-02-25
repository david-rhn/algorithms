def merge_sort(arr: list) -> list:
    """ Function which sorts an array using the merge sort algorithm.

    The merge sort algorithm works in the following way:
    1. Recursively divides the array into two halves.
    2. Sorts each half.
    3. Merges the sorted halves back together.

    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        (list): A new sorted list containing the elements of the input list in ascending order.

    Time Complexity: O(n log n)
    """

    # If the array contains one or zero elements its already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index.
    mid = len(arr) // 2

    # Sort the left half.
    left_half = merge_sort(arr[:mid])

    # Sort the right half.
    right_half = merge_sort(arr[mid:])

    # Join the two sorted halves.
    return merge(left_half, right_half)


def merge(left: list, right: list) -> list:
    """ Function which merges two sorted lists into a single sorted list.

    Args:
        left (list): Left halve sorted list.
        right (list): Right halve sorted list.

    Returns:
        (list): Merged sorted list.
    """

    sorted_list = []

    # Pointers for left and right lists
    i = j = 0

    # Merge elements from left and right lists in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements (if any) from left and right lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

if __name__ == "__main__":

    # Test Case 1: Normal list
    assert merge_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

    # Test Case 2: Already sorted list
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test Case 3: Reverse sorted list
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test Case 4: List with duplicate values
    assert merge_sort([4, 2, 4, 3, 1, 2]) == [1, 2, 2, 3, 4, 4]

    # Test Case 5: List with all identical values
    assert merge_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]

    # Test Case 6: Single element list
    assert merge_sort([42]) == [42]

    # Test Case 7: Empty list
    assert merge_sort([]) == []

    # Test Case 8: List with negative numbers
    assert merge_sort([-3, -1, -4, -2, 0, 2, 1]) == [-4, -3, -2, -1, 0, 1, 2]

    print("All test cases passed!")
