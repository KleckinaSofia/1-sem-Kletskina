# 8. В исходном текстовом файле (Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re
p = re.compile(r"«(.*?)»", re.S)
g = []
for i in open('Dostoevsky.txt').read().split('\n'):
    if len(p.findall(i)) > 0:
        g.append(p.findall(i))
p = []
for i in g:
    for o in i:
        p.append(o)
a = 0
for i in set(p):
    print(i)
    a += 1
print(a)
