import sys

data = [int(sys.stdin.readline()) for i in range(9)]

print(max(data))
print(data.index(max(data))+1)