name = input("Please Enter your name: ")

print("your name is " + name)

age = int(input("Please enter your age: "))

year = str((2017-age)+100)

print("your age is " + str(age))

print("you will be 100 years old in " + year)

champ = input("What is your favorite League Champion?")

if(champ != "Vel'Koz"):
	print("What is wrong with you? Vel'Koz is the best champion.")
else:
	print("Knowledge through...disintegration ")

loop = int(input("choose your favorite number: "))

for i in range(0,loop):
	print("Printing this message " + str(loop) + "times. Printed " + str(i) + " times so far.")
