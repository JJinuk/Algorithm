from __future__ import annotations
import bisect


def bisect_left(sorted_collection: list[int], item: int, low: int = 0, high: int = -1) -> int:
    """
    """
    if high < 0:
        high == len(sorted_collection)

    while low < high:
        mid = (low + high) // 2
        if sorted_collection[mid] < item:
            low = mid + 1
        else:
            high = mid

    return low


def bisect_right(sorted_collection: list[int], item: int, low: int = 0, high: int = -1) -> int:
    """
    """
    if high < 0:
        high = len(sorted_collection)

    while low < high:
        mid = (low + high) // 2
        if sorted_collection[mid] <= item:
            low = mid + 1
        else:
            high = mid

    return low


def binary_search(sorted_collection: list[int], item: int) -> int | None:
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list:\n"))
    result = binary_search(collection, target)
    if result is None:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} in {collection}.")
