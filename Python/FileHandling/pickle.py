import pickle,saapadu

f=open("objects.dat",'w+b',-1)
s=saapadu.Saapadu("Phal","Rendu","mupadhu")
pickle.dump(s,f)
f.close()
