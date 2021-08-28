from itertools import combinations

# print list(combinations(['a', 'a', 'c', 'd'], 2))

n, l, k = int(input()), input().strip().split(' '), int(input())

c = 0.0
lc = 0.0

for i in combinations(l, k):
    lc += 1
    if 'a' in i:
        c += 1

print ("%.3f" % (c / lc))
