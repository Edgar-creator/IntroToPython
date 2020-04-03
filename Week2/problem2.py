str = input().lower().split(" ")
d = {}
l = {}
s = {}
for i in str:
    if i in d:
        d[i].append(i)
    else:
        d[i] =[i]
for i in d:
    l[i] = len(d[i])
for key in l.keys():
    if l[key] in s:
        s[l[key]].append(key)
    else:
        s[l[key]] = [key]
n = max(s.keys())
for i in s[n]:
    print(i,n)