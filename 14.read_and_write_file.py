#****************Read and Write in file(r+)**********

f=open("anil.txt","r+")#r+ access mode is use for both read and write in file
f.write("hello anil how are you! \n")#save this input in anil.txt
print(f.read())#read and print the input from anil.txt

f.close()
