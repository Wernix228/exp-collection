#2
s = input()
cnt = 0
while ":" in s:
    s = s.replace(":","%",1)
    cnt+=1
print(cnt)
#7
s = input()
l = len(s)//2
st = s[:l]
st = st.replace("п","*")
s = st + s[l:]
print(s)
#12
print([y for y in [x for x in input().split(" ")] if y[-1] == "я"])