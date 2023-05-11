n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

def check(x, y, n):
    curr = graph[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if curr != graph[i][j]:
                print("(", end="")
                next_n = n // 2
                check(x, y, next_n)                
                check(x, y + next_n, next_n)       
                check(x + next_n, y, next_n)      
                check(x + next_n, y + next_n, next_n)  
                print(")", end="")
                return
    if curr == 1:
        print(1, end="")        
    else:
        print(0, end="")
    
check(0, 0, n)
