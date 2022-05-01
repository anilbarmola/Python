# Dictionary in python #key:vlaue
dr = {"NAME": "anil barmola", "AGE": "27",
      "MOBILE": "8984060915", "ROLL NUM": "17"}
print(dr)
print(dr["NAME"])  # get value by calling key
# ********print all key using for loop
for n in dr:
    print(n)
print("*********** print all value in dictiony by using for loop")
for n in dr:
    print(dr[n])

# **************function in dictionary ***get()**keys()****value()*****itmes()
print("***********function in dictioney********")
n = dr.get("MOBILE")
print(n)

print("keys:-")
for a in dr.keys():
    print(a)

print("print value only")
for d in dr.values():
    print(d)

print("item in dictionary")
for a, b in dr.items():
    print(a, ":", b)

print("DEL key word in Python")
print(dr)
dr.pop("MOBILE")
print(dr)