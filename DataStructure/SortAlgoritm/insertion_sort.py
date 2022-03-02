array = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
        print(array[:i+1])


print("before:", array)
insertion_sort(array)
print("after:", array)