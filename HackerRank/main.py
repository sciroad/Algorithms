from collections import Counter, defaultdict
dist = defaultdict(lambda : Counter(""))
fact = dict()
powr = dict()
m = 10 ** 9 + 7
def initialize(s):
    fact[0], powr[0], dist[0] = 1, 1, Counter(s[0])
    for j in range(1, len(s)):
        fact[j] = (j * fact[j - 1]) % m
        dist[j] = dist[j-1] + Counter(s[j])

initialize("aabb")
print(dist)