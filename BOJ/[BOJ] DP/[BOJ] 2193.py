n = int(input())
arr = [0, 1, 1]

for i in range(3, 91):
    arr.append(arr[i-1] + arr[i-2])

print(arr[n])
