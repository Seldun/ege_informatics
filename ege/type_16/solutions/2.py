'''
Алгоритм вычисления функций F(n) и G(n) задан следующими соотношениями:
		F(n) = G(n) = 1 при n = 1
		F(n) = F(n–1) + 3 · G(n–1), при n > 1
		G(n) =  F(n–1) – 2 · G(n–1), при n > 1
Чему равна сумма цифр значения функции F(18)?

'''

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) + 3 * G(n-1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) - 2*G(n-1)

number = F(18)

# summ = 0
# for i in str(number):
#     summ += i
summ = sum(int(i) for i in str(number))
print(summ)