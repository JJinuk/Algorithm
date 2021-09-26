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
