n = int(input())
paper = []

for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

white_cnt, blue_cnt = 0, 0

def check(row, col, n):
    global white_cnt, blue_cnt
    curr = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if curr != paper[i][j]:
                next_n = n//2
                check(row, col, next_n)
                check(row, col+next_n, next_n)
                check(row+next_n, col, next_n)
                check(row+next_n, col+next_n, next_n)
                return
            
    if curr == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
    return

check(0, 0, n)
print(f'{white_cnt}\n{blue_cnt}')