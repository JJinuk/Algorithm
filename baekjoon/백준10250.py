import sys

t = int(sys.stdin.readline())

for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    room = n//h + 1                                     # 방 번호: n를 h로 나눈 몫 + 1
    floor = n % h                                       # 층 수: n을 h로 나눈 나머지

    if n % h == 0:                                      # n이 h의 배수일 경우
        room = n//h
        floor = h
    print(f'{floor*100+room}')
