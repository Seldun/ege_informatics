'''
3.	Алгоритм вычисления функции F(n) задан следующими соотношениями:
F(n) = n при n ≤ 3;
F(n) = F(n – 1) + 2 · F(n / 2)  при чётных n >3; 
F(n) = F(n – 1) + F(n – 3)  при нечётных n > 3;
Определите количество натуральных значений n, при которых F(n) меньше, чем 10^8

'''
from functools import *
from sys import *

setrecursionlimit(10**9)
@lru_cache(maxsize=None)
def F(n):
    if n <= 3:
        return n
    if n % 2 == 0 and n > 3:
        return F(n - 1) + 2 * F(n / 2)
    if n % 2 != 0 and n >3:
        return F(n - 1) + F(n - 3)
    
cnt = 0
for n in range(1,10_000):# надо для проверки потом увеличить range(1,100_000) для проверки измениться ли ответ
    if F(n) < 10**8:
        cnt += 1

print(cnt)