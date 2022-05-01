#********** string function************
#*********** find(), index() , isalpha(), isdigit(), isalnum()*******
a="hello anil how are you keep going with python 123"
print(a.find("a"))#a is at 6th place from stating point
print(a.find("a",3))# find a from 3ed  start from 3ed place of string
print(a.index("a"))# index will work as same. find fuction but index show error while find gives -1 when do not found the value
b="12hello"
print(b.isalnum())
