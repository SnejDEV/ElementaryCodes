vowel=0
conso=0
inp =  (input("Enter String: ").strip()).lower()

v="aeiou"

for letter in inp:
    if letter in v:
        vowel=vowel+1
    elif (ord(letter) in range(97,122)) and (not(letter in v)):
        conso=conso+1

print("Consonents = {}".format(conso))
print("Vowels = {}".format(vowel))
