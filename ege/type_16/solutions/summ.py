def summ(n):
    if n < 10:
        return n
    if n >= 10:
        return n%10 + summ(n//10)


print(summ(115))
