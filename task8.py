import random
import math

#2_1
mtrx = []
#sozdanie matrici
for y in range(0,3):
    a = []
    for x in range(0,3):
        a.append(random.randint(1,2))
    mtrx.append(a)
for i in mtrx:
    print(i)
#proverka
#po linii
notMagic = False
tmp = sum(mtrx[0])
for xd in mtrx:
    if sum(xd) != tmp:
        notMagic = True
#po stolbcu
summ = []
tmp = 0
for y in range(0,len(mtrx)):
    for x in range(0, len(mtrx[y])):
        tmp += mtrx[x][y]
    summ.append(tmp)
    tmp = 0
for i in range(len(summ)-1):
    if summ[i] != summ[i+1]:
        notMagic = True
print("no" if notMagic else "yes")
#2_2
for ln in mtrx:
    tmp = ln[0]
    ln[0] = ln[len(mtrx)-1]
    ln[len(mtrx)-1] = tmp
for ln in mtrx:
    print(ln)
#7_1
def triang_to_mtrx(n, arr):
    mtrx = [[0]*n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i, n):
            mtrx[i][j] = arr[k]
            mtrx[j][i] = arr[k]
            k += 1
    return mtrx
#7_2
def magicMatric(mtrx):
    diag = [mtrx[i][i] for i in range(len(mtrx))]
    trace = sum(diag)

    for i in range(len(mtrx)):
        if i % 2 == 0:
            for j in range(len(mtrx)):
                mtrx[i][j] = mtrx[i][j] / trace
    for i in mtrx:
        print(i)