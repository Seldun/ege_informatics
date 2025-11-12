
def f(s,c,m):
    if s > 45:
        return c%2 == m%2
    elif c == m:
        return False

    arr = []
    for k in range(2,s+1):
        if s % k == 0:
            arr.append(f(s + s//k,c+1,m))

    return any(arr) if (c+1)%2 == m%2 else all(arr)


print([s for s in range(2,46) if not(f(s,0,1)) and f(s,0,2)])
print([s for s in range(2,46) if not(f(s,0,1)) and f(s,0,3)])
print([s for s in range(2,46) if f(s,0,4) and not(f(s,0,2))])
