import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a = sys.stdin.readline().strip()
    stack = []
    # 괄호 판별을 위한 반복문
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            # 스택에 아무것도 없는 경우
            if len(stack) == 0:
                print("NO")
                break
            # 스택에 뭐라도 있는 경우
            else:
                stack.pop()
    # break문이 걸리지 않으면 for-else를 이용해서 한번 더 체크, 최종 결과값인 YES/NO를 판별
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
