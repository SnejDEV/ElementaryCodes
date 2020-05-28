films={"Vada chennai":[18,10],
       "Comali":[3,10],
       "Petta":[13,10]
      }
while True:

    m=(input("Enter the movie name: ").strip()).capitalize()

    if(m in films):
        if(films[m][1]>0):
            a=int(((input("Enter age: ")).strip()))
            if(a>=films[m][0]):
                    c=(input("Do you want to confirm booking?(y/n): ").strip()).lower()
                    if(c=='y'):
                        print("Ticket booked :)")
                    elif(c=='n'):
                        print("You have'nt confirmed ur ticket :(")
                    else:
                        print("Invalid Entry")
            elif(a<=films[m][0]):
                print("You are too young to watch the film uve chose")
            else:
                print("Invalid Entry")
        elif(films[m][1]==0):
            print("Tickets sold out!")
        else:
            print("Invalid Entry")
    else:
        print("Sorry movie not available :(")
        
