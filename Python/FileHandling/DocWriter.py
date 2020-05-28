f=open("E:\Python_Bible\Advanced_Python\Files_new\Reference.docx","r")
s=''
print("To exit document, enter '#'")
'''while(s!='#'):
     s=str(input())
     if(s=='#'):
          continue
     f.write(s+'\n')'''
s=f.read()
print(s)
f.close()
