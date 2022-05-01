#******************** altration of stirig*********
b="how alteration work in python"
#********* b=[-1::-1]******reverse the str
t=len(b)
print(t)
for item in range(t):
    print(b[item])

print("************revers the loop***********")
for item in range(t-1,-1,-1):
    print(b[item])