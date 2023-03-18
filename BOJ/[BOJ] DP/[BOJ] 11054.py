import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp_increase = [1] * N

reversed_A = list(reversed(A))
dp_decrease = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
        if reversed_A[i] > reversed_A[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

res = []
for i in range(N):
    res.append(dp_increase[i] + dp_decrease[N-i-1]-1)

print(max(res))