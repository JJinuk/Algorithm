import sys

A = int(sys.stdin.readline())   # 첫번째 입력: 숫자 변환
B = sys.stdin.readline()        # 두번째 입력: 문자열 그대로

# 문자열 인덱스 이용, B를 하나씩 숫자로 변환 후 A와 곱한다
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')