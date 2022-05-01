#*******************zip function ***************
l=[1,2,3,4]
m=[5,6,7,8]# both list have same element otherwise zip avoid extra element
for a,b in zip(l,m):
    print(a,b)

print("*************iterate by for loop********")
t=len(l)
for h in range(t):
    print(l[h],m[h])