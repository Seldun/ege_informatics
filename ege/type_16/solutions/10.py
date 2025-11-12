'''10.	Алгоритмы вычисления функций F(n) и G(n) заданы следующими соотношениями (здесь // – операция деления нацело, % – остаток от деления):
F(n) = n, при n < 10,
F(n) = F(G(n)), при n ≥ 10,
G(n) = n, при n < 10,
G(n) = n % 10 + G(n // 10), при n ≥ 10.
Чему равно значение F(12345678987654321)?

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def G(n):
    if n < 10:
        return n
    return n % 10 + G(n // 10)

@lru_cache(maxsize=None)
def F(n):
    if n < 10:
        return n
    return F(G(n))

print(F(12345678987654321))