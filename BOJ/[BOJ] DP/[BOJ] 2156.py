import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)] 

arr = [0]
arr.append(wine[0])
if (n > 1):
    arr.append(wine[0] + wine[1])
    
for i in range(3, n+1):
    arr.append(max(wine[i-1] + arr[i-2], wine[i-1] + wine[i-2] + arr[i-3], arr[i-1]))

print(arr[n])



    # 연속 3잔 마시면 안된다.
    # case1: i-1잔을 안마셨을 때: i-2까지의 최대값(arr[i-2])에 wine[i-1]을 더해준다.
    # case2: i-2잔을 안마시고, i-1잔을 마셨을 때: i-3까지의 최대값(arr[i-3])에 wine[i-2]과 wine[i-1]을 더해준다.
    # case3: i-2잔과 i-1잔을 모두 마신 경우: i-1까지의 최대값(arr[i-1])
    # 위 세가지를 고려하여 max

    # case_1 = wine[i-1] + arr[i-2]
    # case_2 = wine[i-1] + wine[i-2] + arr[i-3]
    # case_3 = arr[i-1]
    # max_value = max(case_1, case_2, case_3)