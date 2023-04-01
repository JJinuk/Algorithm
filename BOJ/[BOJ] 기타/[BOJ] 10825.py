import sys

n = int(sys.stdin.readline())
grade = [list(sys.stdin.readline().split()) for _ in range(n)]

grade.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in grade:
    print(i[0])