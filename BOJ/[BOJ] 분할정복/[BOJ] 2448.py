n = int(input())

def star(a):
    if a == 3:
        return ['  *  ',' * * ','*****']
    
    arr = star(a//2)
    stars = []
    
    for i in arr:
        stars.append(' '*(a//2)+i+' '*(a//2))
    for i in arr:
        stars.append(i+' '+i)
    return stars

print('\n'.join(star(n)))