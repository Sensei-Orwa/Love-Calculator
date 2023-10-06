print("Welcome to the love calculator!")

#VARIABLES
name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")

combined_string = name1 + name2
Lower = combined_string.lower() #To cover up for upper & lower case

t = Lower.count("t")
r = Lower.count("r")
u = Lower.count("u")
e = Lower.count("e")
total1 = t + r + u + e

l = Lower.count("l")
o = Lower.count("o")
v = Lower.count("v")
e = Lower.count("e")
total2 = l + o + v + e

score = str(total1) + str(total2)

print(f"Your score is {score}")











