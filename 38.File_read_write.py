#*********PICKLE library*************
#********store and read data using pickle library************** 
import pickle
lst=[10,20,30,40,50]
file=open("anil.txt","rb")
#pickle.dump(lst,file)     # stroe data inside file in syncynize foam. user wb format
#print(pickle.load(file))  # read data using rb format
file.close()