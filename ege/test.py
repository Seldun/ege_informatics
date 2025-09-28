from itertools import *

cnt = 0
for i in product(sorted("СТРОКА"), repeat=5):
    cnt += 1
    i = "".join(i)
    if i[0] not in "АСТ" and i.count("О") == 2 and cnt % 2 == 0:
        print(cnt, i)