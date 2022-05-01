#***************seek and tell in file****************

f=open("anil.txt")
print(f.read(), end="")
print(f.tell())#tell explain where is pointer now
print(f.seek(16))#seek move point at give charchter (16)
print(f.read())
f.close()
