n = int(input())

def star(a):
    if a == 3:
        return ['***', '* *', '***']
    arr = star(a//3)
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(a//3)+i)    
    for i in arr:
        stars.append(i*3)
    return stars

print('\n'.join(star(n)))
