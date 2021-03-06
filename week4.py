import sys


class Hash:
    def __init__(self):
        self.len = 1
        self.table = [set()]
        self.used = 0

    def __repr__(self):
        message = ""
        count = 0
        for i in self.table:
            message += str(count) + ":"
            count += 1
            message += str(i) + "\n"
        return message

    def search(self, e):
        if e:
            for i in self.table:
                if e in i:
                    return True
        return False

    def insert(self, e):
        if e:
            key = int(e % self.len)
            if self.used > 0.75 * self.len:
                self.rehash(self.len * 2)
            self.table[key].add(e)
            self.used += 1

    def delete(self, e):
        if e:
            for i in self.table:
                if e in i:
                    i.remove(e)
                    self.used -= 1
                    return True
        return False

    def rehash(self, new_len):
        print("Rehashing")
        print(self)
        oldTable = self.table

        self.table = []
        self.len = new_len
        for i in range(new_len):
            self.table.append(set())
        for i in oldTable:
            for s in i:
                self.table[int(s % self.len)].add(s)


import random

sys.setrecursionlimit(100000000)
t = Hash()
print("*" * 10, "CHAIN HASH", "*" * 10)
print("*" * 10, "INSERTING", "*" * 10)
temp = []
for i in range(200):
    temp.append(random.uniform(0, 1000))
    t.insert(temp[i])
print("*" * 10, "DONE INSERTING", "*" * 10)
ready_to_delete = []
while len(ready_to_delete) <= 100:
    element = random.choice(temp)
    ready_to_delete.append(element)
    temp.remove(element)

print("*" * 10, "READY TO DELETE", "*" * 10)
for i in ready_to_delete:
    print(i, "FOUND ", t.search(i))

print("DELETING")
for i in ready_to_delete:
    t.delete(i)

for i in ready_to_delete:
    print(i, "FOUND ", t.search(i))

print("*" * 10, "DONE DELETING", "*" * 10)
print(t)
print("*" * 10, "END CHAIN HASH", "*" * 10)

hashdict = dict()
while (True):
    r = random.random()
    if r not in hashdict.values():
        hr = hash(r) % (2 ** 32)
        if hr in hashdict.keys():
            print(repr(r) + ", " + repr(hashdict[hr]) + ": " + repr(hr))
            break
        hashdict[hr] = r


def B(n, k):
    C = [0 for i in range(k + 1)]
    C[0] = 1  # since nC0 is 1

    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j - 1]
            print(C[j], end=' ')
            j -= 1
        print()
    return C[k]


print((B(50, 100)))  # 184756


# https://en.wikipedia.org/wiki/Change-making_problem

def f(n):
    assert type(n) == int
    assert n <= 1000
    actual_amount = 0
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    minCoins = [[0 for _ in range(n + 1)] for _ in range(len(coins) + 1)]
    for i in range(n + 1):
        minCoins[0][i] = i
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            if coins[c - 1] == r:
                minCoins[c][r] = 1
            elif coins[c - 1] > r:
                minCoins[c][r] = minCoins[c - 1][r]
            else:
                minCoins[c][r] = min(minCoins[c - 1][r], 1 + minCoins[c][r - coins[c - 1]])

    return minCoins[-1][-1]


print(f(25))
