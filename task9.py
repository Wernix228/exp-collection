# A
# 7
import random

A = int(input())
B = int(input())
def m(a,b):
    if a == b:
        print(a)
        return
    print(a)
    m(a+1,b)
def bo(a,b):
    if a == b:
        print(a)
        return
    print(a)
    bo(a-1, b)

if(A < B):
    m(A,B)
else:
    bo(A,B)
print("====================================")
# B
# 3
a = []
i = random.randint(0,10)
while i != 0:
    a.append(i)
    i = random.randint(0,10)
else:
    a.append(0)
print(a,'\n')

def recur(a,i):
    if i == len(a)-1:
        return
    if i % 2 == 1:
        print(a[i])
    recur(a,i+1)
recur(a,0)