import math
def tr(x,y,z):
    p = (x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s
#2_1
def f(a):
    print(tr(a,a,a)*6)
#2_2
def f2(a,b):
    c = math.sqrt(a**2+b**2)
    print(tr(a,b,c)*3)
#7_1
def f3(X,Y):
    return (X*Y)/2

def sqare(X,Y,Z,T):
    return f3(X,Y)+f3(Z,T)
# 7_2
def to_eight(i):
    return oct(i)[2:].zfill(10)
print(to_eight(int(input())))



