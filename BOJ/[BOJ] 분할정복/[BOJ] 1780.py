n = int(input())
minus, zero, one = 0, 0, 0
paper = []

for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

def check(row, col, n):
    global minus, zero, one
    curr = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)                         #1 (0,0)
                check(row, col+next_n, next_n)                  #2 (0,1)
                check(row, col+(next_n*2), next_n)              #3 (0,2)
                check(row+next_n, col, next_n)                  #4 (1,0)
                check(row+next_n, col+next_n, next_n)           #5 (1,1)
                check(row+next_n, col+(next_n*2), next_n)       #6 (1,2)
                check(row+(next_n*2), col, next_n)              #7 (2,0)
                check(row+(next_n*2), col+next_n, next_n)       #8 (2,1)
                check(row+(next_n*2), col+(next_n*2), next_n)   #9 (2,2)
                return
            
    if curr == -1:
        minus += 1
    elif curr == 0:
        zero += 1
    else:
        one += 1
    return

check(0, 0, n)
print(f'{minus}\n{zero}\n{one}')