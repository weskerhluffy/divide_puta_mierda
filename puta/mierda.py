'''
Created on 13/04/2018

@author: ernesto
'''

# XXX: https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/practice-problems/algorithm/divide-apples/

N = int(input())
n = [int(x) for x in input().strip().split(" ")]
m = sum(n) // len(n)
n_len = len(n)
# print("n_len {}".format(n_len))
#print("lista antes {}".format(n))
n = list(map(lambda x:x - m, n))
print("lista despues {}".format(n))
r = 0
b = [0] * n_len
for i, x in enumerate(n[:-1]):
    b[i + 1] = b[i] + n[i]
    
print("b {}".format(b))

b.sort()

med = -b[n_len >> 1]

print("b {} med {}".format(b, med))
for bi in b:
    r += abs(bi + med)

print(r)
