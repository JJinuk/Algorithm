from collections import defaultdict


# import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


HASHMAP_SIZE = 1000


class HashMap:
    # 초기화
    def __init__(self):
        self.size = HASHMAP_SIZE
        self.table = defaultdict(ListNode)

    # def _hash()

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # index 값이 비어 있을 때
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # index 값이 채워져 있을 때
        p = self.table[index]
        while p:  # p == None -->
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size

        # 비어 있다면
        if self.table[index].value is None:
            return -1
        # 링크드 리스트가 있다면
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size

        # 비어있는 경우
        if self.table[index].value is None:
            return

        # 링크드리스트의 첫번째, head
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
            # 중간에 있는 경우에는, 전, 다음꺼를 연결해주는 경우
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
