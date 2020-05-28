#basic db creation
a={"Snehal":{"Id":1,"Cb":"Poor"},"Hemal":{"ID":2,"Cb":"Excellent"}}
#input
c=input("Enter Name: ")
b=input("Enter Key(id/cb): ")
#print
print(a[((c.strip()).capitalize())][((b.strip()).capitalize())])
