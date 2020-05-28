#List of names
db = []

#Enter name
print("Hello I'm Travis :)")

#loop
while(True):

    name = (input("What is your name? ").strip()).capitalize()

    #Checking db
    if(name in db):
        print("Hello {}".format(name))
        rem = (input("Do u want to leave the db?(y/n) ")).lower()
        if(rem == 'y'):
            db.remove(name)
        elif(rem =='n'):
            print("Neither did i want u to leave")
        else:
            print("I guess u've entered something wrong")
    else:
        print("I dont think I've met you before {}".format(name))
        rem = input("Would u like to be added to the db?(y/n) ")
        if(rem == 'y'):
            db.append(name)
        elif(rem =='n'):
            print("No probs, see ya")
        else:
            print("I guess u've entered something wrong")
