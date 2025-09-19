A = int(input())
B = int(input())

# 2
if(A < B):
    for i in range(A,B + 1):
        print(i)
else:
    for i in range(A,B -1,-1):
        print(i)

# 7
N = int(input())
t = 1
res = 0
for i in range(1,N+1):
    t = t * i
    res = res + t
print(res)

# XD