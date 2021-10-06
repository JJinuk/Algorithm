# 보통 N/2 진행하지만 N/3+1이 더 빠르다
array = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]


def shell_sort(array):
    while gap > 0:
        i = 0
        j = gap

        # 왼쪽에서 오른쪽으로 배열 확인
        # 가능한 j의 마지막 인덱스까지
        while j < len(array):

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

            i += 1
            j += 1
            # i번째 인덱스부터 왼쪽으로 돌아본다
            # 정렬되지 않은 값들을 바꿔준다.
            k = i
            while k - gap > -1:
                if array[k - gap] > array[k]:
                    array[k - gap], array[k] = array[k], array[k - gap]
                k -= 1


        gap //= 3
    gap = len(array) // 3 + 1                               # gap 초기화



print("before:", array)
shell_sort(array)
print("after:", array)


