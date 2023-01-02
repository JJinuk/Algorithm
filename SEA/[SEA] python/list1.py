# 인덱싱(하나의 요소를 인덱스 연산자를 통해 참조)

arr = [4, 5, 6, 7, 8, 9]
print(arr[0])  # 4
print(arr[-1])  # 9

# 슬라이싱(원하는 범위 선택 연산)
print(arr[1:3])  # [5, 6]
print(arr[:3])  # [4, 5, 6]
print(arr[1:])  # [5, 6, 7, 8, 9]
print(arr[:])  # [4, 5, 6, 7, 8, 9]

# 10보다 작은 짝수들의 집합을 원소로 하는 리스트
mylist = [2, 3, 4, 5, 6]
newlist = [i for i in mylist if i % 2 == 0]
print(newlist)  # [2, 4, 6]
