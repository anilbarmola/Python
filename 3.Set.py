#Set in python
from re import S
from typing import Set


S=set({1,2,3})
S1=set({2,3,4,5})

print(S, S1)
print("Union of set " ,S.union(S1))
print("intersection of set ", S.intersection(S1))
S.clear()
print(S)
S.add(6)
print(S)

