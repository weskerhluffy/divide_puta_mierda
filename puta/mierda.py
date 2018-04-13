'''
Created on 13/04/2018

@author: ernesto
'''

N = int(input())
n = [int(x) for x in input().strip().split(" ")]
m = sum(n) // len(n)
n_len = len(n)
modm = lambda x:x % n_len
valleys = []

f = 0
i = 0
while i < n_len:
    if n[i] > m:
        break
    i += 1
    
if i < n_len:
    f = i

    i = modm(i + 1)
    while i != f:
        print("i {}".format(i))
        if n[i] < m:
            break
        if n[i] > m:
            f = i
        i = modm(i + 1)
        
    print("f {}".format(f))
    
    i = f
    j = modm(i + 1)
    exita = False
    while not exita:
        exita = False
        while j != i:
            if n[j] < m:
                break
            j = modm(j + 1)
            if j == f:
                exita=True
        valley = (i, j)
        valleys.append(valley)
        i = j
        j = modm(i + 1)
        lj = i
        while j != i:
            if n[j] > m:
                break
            if n[j] < m:
                lj = j
            j = modm(j + 1)
            if j == f:
                exita=True
        valley = (i, lj)
        valleys.append(valley)
        i = j
        j = modm(i + 1)
        lj = i
        while j != i:
            if n[j] < m:
                break
            if n[j] > m:
                lj = j
            j = modm(j + 1)
            if j == f:
                exita=True
        i = lj
    print("valleys {}".format(valleys))
