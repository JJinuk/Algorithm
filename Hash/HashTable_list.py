hash_table = list([0 for i in range(10)])   # 해쉬 테이블 공간 생성


def get_key(data):                              # 해쉬 키 생성
    return hash(data)


def hash_function(key):                         # Division 이용한 간단한 해쉬 함수
    return key % 10


def save_data(data, value):
    hash_address = hash_function(get_key(data)) # 해쉬 함수로 산출한 해시 주소
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]



