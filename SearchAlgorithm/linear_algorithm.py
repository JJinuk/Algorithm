def linear_search(sequence: list, target: int) -> int:
    """
    parm sequence: 비슷한 item이 있는 collection(선형 탐색 정렬된 item)
    parm target: 검색할 item의 값
    return: 찾은 item의 index 또는 item이 없는 경우
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1


def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """
    param low: 배열의 하한
    param high: 배열의 상한
    param target: 찾기위한 요소
    return: 키 인덱스 or 키를 찾을 수 없는 경우 -1
    """
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise Exception("Invalid upper or lower bound!")
    if high < low:
        return -1
    if sequence[low] == target:
        return low
    if sequence[high] == target:
        return high
    return rec_linear_search(sequence, low + 1, high - 1, target)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]

    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = linear_search(sequence, target)
    if result != -1:
        print(f"linear_search({sequence}, {target}) = {result}")
    else:
        print(f"{target} was not found in {sequence}")
