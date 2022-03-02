n = 1260
count = 0

# 큰 단위 화폐부터 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin              # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 화폐의 종류를 K라 할 때 시간 복잡도는 O(k)
# 시간 복잡도는 동전의 총 종류에만 영향, 거스름 돈의 크기와 무관

