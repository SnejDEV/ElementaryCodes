from random import choice

l=["Why is the sky blue?","How to become god?","How different is a male from female?"]
q=choice(l)

q1=(input(q+": ").strip()).lower()

while(q1!= "just because"):
        q1=(input("But why? ").strip()).lower()

print("Ok")        
    
