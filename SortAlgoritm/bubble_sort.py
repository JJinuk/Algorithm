array = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(array)


print("before:", array)
bubble_sort(array)
print("after:", array)