hash_table = list([0 for i in range(10)])  # 해쉬 테이블 공간 생성


def get_key(data):  # 해쉬 키 생성
    return hash(data)


def hash_function(key):  # Division 이용한 간단한 해쉬 함수
    return key % 10


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)  # 해쉬 함수로 산출한 해시 주소

    # 1. 해시 충돌이 발생할 경우 (해시 주소가 동일한 경우)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            # 1-1. key가 동일하면 데이터를 덮어쓴다.
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
            # 1-2. key가 동일하지 않으면 데이터를 연결해 저장
            hash_table[hash_address].append([index_key, value])
        # 2. 해시 충돌이 발생하지 않으면 그 공간에 데이터(key, value)를 저장
        else:
            hash_table[hash_address] = [[index_key, value]]

    def read_data(data):
        index_key = get_key(data)
        hash_address = hash_function(index_key)

        if hash_table[hash_address] != 0:
            for index in range(len(hash_table[hash_address])):
                if hash_table[hash_address][index][0] == index_key:
                    return hash_table[hash_address][index][1]
                return None
            else:
                return None
