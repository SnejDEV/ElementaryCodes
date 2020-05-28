'''word = (input("Enter a word: ")).strip()

vowel="aeiou"
conso=""
v=0

for l in word:
    if(l in vowel):
        vp=word.index(l)
        break
    else:
        conso=conso+l

print((word[vp:])+conso)  '''

'''word = (input("Enter a sentence: ")).strip()
conso,fs,a,vp="","",0,0

for l in word:
    if(l != " "):
        if(l in "aeiou" and a==0):
            vp=word.index(l)
            a=1
        elif(a==0):
            conso = conso+l
    elif(l == " "):
         fs=fs+(word[vp:word.index(l)]+conso)+" "
         conso=""
         vp=0
         a=0
        
print(fs)
'''

sent = input("Enter a Sentence: ").strip().lower()
words = sent.split()            

conso,c,vp="",0,0

for word in words:
    conso,vp="",0
    for l in word:
        if l in 'aeiou':
            vp = word.index(l)
            break
        else:
            conso=conso+l

    w=word[vp:]+conso
    w= (w+"yay") if(w==word) else w+"ay" 
    words[c]=w
    c=c+1

out=" ".join(words)
print(out)

























