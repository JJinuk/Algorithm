tc = input()

for i in range(97, 123):
    if chr(i) in tc:
        print(tc.count(chr(i)), end=' ')
    else:
        print(0, end=' ')