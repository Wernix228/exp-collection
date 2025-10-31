def getMtrx(name):
    mtrx = []
    with open(name, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            mtrx.append(row)
    return mtrx
def vivodMtrx(mtrx,name):
    f = open(name, "w")
    for ln in mtrx:
        for w in ln:
            f.write(str(w) + " ")
        f.write('\n')
def t2_1():
    mtrx = getMtrx("vvod2_1.txt")
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
    f = open("vivod2_1.txt","w")
    a = ("no" if notMagic else "yes")
    f.write(a)
def t2_2():
    mtrx = getMtrx("vvod2_1.txt")
    for ln in mtrx:
        tmp = ln[0]
        ln[0] = ln[len(mtrx) - 1]
        ln[len(mtrx) - 1] = tmp
    # f = open("vivod2_2.txt", "w")
    # for ln in mtrx:
    #     for w in ln:
    #         f.write(str(w) + " ")
    #     f.write('\n')
    vivodMtrx(mtrx,"vivod2_2.txt")
def t7_1():
    mtrx = getMtrx("vvod2_1.txt")
    for ln in mtrx:
        tmp = ln[0]
        ln[0] = ln[len(mtrx) - 1]
        ln[len(mtrx) - 1] = tmp
    # f = open("vivod7_1.txt","w")
    # for ln in mtrx:
    #     for w in ln:
    #         f.write(str(w) + " ")
    #     f.write('\n')
    vivodMtrx(mtrx, "vivod7_1.txt")
def t7_2():
    mtrx = getMtrx("vvod2_1.txt")
    diag = [mtrx[i][i] for i in range(len(mtrx))]
    trace = sum(diag)

    for i in range(len(mtrx)):
        if i % 2 == 0:
            for j in range(len(mtrx)):
                mtrx[i][j] = mtrx[i][j] / trace
    vivodMtrx(mtrx,"vivod7_2.txt")
if __name__ == "__main__":
    t2_1()
    t2_2()
    t7_1()
    t7_2()
