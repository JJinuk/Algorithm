# A, B, C, D = input().split()
#
# print(int(A+B) + int(C+D))
# input은 입력하는 모든 것들을 문자열로 취급
import sys

A, B, C, D = sys.stdin.readline().split()

print(int(A+B) + int(C+D))