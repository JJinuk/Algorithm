def countingSort(arr, digit):
    n = len(arr)

    # 배열의 크기에 맞는 output 배열 생성, 10개의 0을 가진 count 배열 생성
    output = [0] * (n)
    count = [0] * (10)

    # digit, 자릿수에 맞는 count += 1
    for i in range(0, n):
        index = int(arr[i]/digit)
        count[index % 10] += 1

    # count배열을 수정하여 digit으로 잡은 포지션을 설정한다
    for i in range(1, 10):
        count[i] += count[i-1]
        print('index:', i, '|', 'value:', count[i])
    # 결과 배열, output 설정, 설정된 count 배열에 맞는 부분 arr 담음
    i = n - 1;
    while i>= 0:
        index = int(arr[i]/digit)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # arr를 결과에 재할당
    for i in range(0, len(arr)):
        arr[i] = output[i]

def RadixSort(arr):
    # arr 배열 중 max 값을 찾아 어느 digit, 자릿수까지 반복하면 될지 정함
    maxValue = max(arr)
    # 자릿수마다 countingSort시작
    digit = 1
    while int(maxValue/digit) > 0:
        countingSort(arr, digit)
        digit *= 10

arr = [222, 96, 123, 1, 23, 5, 2, 17, 28]
RadixSort(arr)

for i in range(len(arr)):
    print([i], arr[i], end=" ")

