import os,sys                 #os is a module which has a submodule named path which in turn has a isFile MeThOd viz is used to check if a file exists
                              #sys is another module used to exit when a file doesnt exit

if(os.path.isfile("E:\Python_Bible\Advanced_Python\Files_new\FileCheckAndWrite\doc.txt")):
     f=open("doc.txt","r+",-1)
else:
     print("File not found")
     sys.exit()                    #Used to exit execution

s=''
print("Enter text: ")
while(s!='#'):
     s=str(input())
     f.write(s)
s=f.read()
print(s)
f.close()







