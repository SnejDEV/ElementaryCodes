#input name
name = input("Enter your name: ")

#input age
age = input("Enter age: ")

#input favourite movie
movie = input("Enter favourite movie: ")

au = "I am {} and my age is {}. {} is my all time favourite movie"
fs = au.format(name,age,movie)

print(fs)
