# OPEN FILE GIVING CORRET INPUT than read and write file.


print("enter the user name(Press 1 to open anil.txt)")
var =int(input())
if var==1:
    print("welcome to anil file : press 1 for read 2 for write")
    pic=int(input())
    if pic == 1:
      print(" read file Mode!")
      f=open("anil.txt","r")
      print(f.read())
      f.close()
    elif pic==2:
      print("tpye data to write inside the file")
      w=input()
      f=open("anil.txt","w")
      f.write(w)
      print("file is updated")
      f.close
    else:
        print("Please give correct input")
else:
    print("user name is not found in database")
