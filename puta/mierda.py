'''
Created on 13/04/2018

@author: ernesto
'''

from queue import PriorityQueue

def dist(sz,a,b):
    m_sz=sz>>1
    d=abs(a-b)
    if d>m_sz:
        d=sz-d
    return d

N = int(input())
n = [int(x) for x in input().strip().split(" ")]
m = sum(n) // len(n)
n_len = len(n)
modm = lambda x:x % n_len
distm=lambda a,b:dist(n_len,a,b)
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
            if j == f:
                exita=True
            j = modm(j + 1)
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
            if j == f:
                exita=True
            j = modm(j + 1)
        valley = (lj,j)
        valleys.append(valley)
        if j==f:
            break
        print("v {}".format(valley))
        i = j
        j = modm(i + 1)
        lj = i
        while j != i:
            if n[j] < m:
                break
            if n[j] > m:
                lj = j
            if j == f:
                exita=True
            j = modm(j + 1)
        i = lj
    print("valleys {}".format(valleys))
    q=PriorityQueue()
    for v in valleys:
      i,j=v
      q.put((distm(i,j),i,j))
