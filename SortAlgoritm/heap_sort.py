def heapify(arr, n, i):
    largest = i                 # 루트를 largest로 초기화
    left_index = 2 * i + 1      # left = 2*i + 1
    right_index = 2 * i + 2     # right = 2*i + 2

    # 루트의 왼쪽 자식 확인
    # 루트보다 클 경우
    if left_index < n and arr[left_index] > arr[largest]:
        largest = left_index

    # 루트의 오른쪽 자식 확인
    # 루트보다 클 경우
    if right_index < n and arr[right_index] > arr[largest]:
        largest = right_index

    # root를 바꾼다(필요하다면)
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]     # swap
        heapify(arr, largest, n)


def heap_sort(arr):
    n = len(arr)
    # 최대 힙을 만든다.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    # 요소를 하나씩 뽑는다
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]         # swap
        heapify(arr, 0, i)
    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(heap_sort(arr))