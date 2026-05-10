from math import *
# Hello World
print("Hello World!")

# making Shapes
print("   /|")
print("  / |")
print(" /  |")
print("/___|")


# Variables:
print("There once was a man named George.")
print("He was 70 years old.")
print("He really liked the name George.")
print("But didn't like being 70.")
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ".")
print("He was " + character_age + " years old.")
character_name = "Mike"
print("He really liked the name " + character_name + ".")
print("But didn't like being " + character_age + ".")


#  STRING
character_name = "Abeera Javaid"

# NUMBER
character_age1 :int = 14

# BOOLEAN
is_female = True

 # WORKING WITH STRINGS
print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\" Academy")
phrase ="Abeera Javaid"
#        012345
print(phrase + " is cool") #  Abeera Javaid is cool
print(phrase.lower()) #  abeera javaid
print(phrase.upper()) # ABEERA JAVAID
print(phrase.upper().isupper()) #  True
print(phrase.isupper()) #  False
print(len(phrase)) # 13
print(phrase[1])   # b
print(phrase.index("Jav"))  # 7
print(phrase.replace("Abeera", "Ramla"))  # Ramla Javaid

# WORKING WITH NUMBERS
print(2) # 2
# Decimal
print(2.568) # 2.568
# Negative
print(-2.568) # -2.568
# Addition
print(3 + 4) # 7
# Multiplication
print(3 * 4) # 12
# Division
print(3 / 4) # 0.75
# Subtraction
print(3 - 4) # -1
# Multi Functions
print(3 * 4 + 5) # 17
print(3 * (4 + 5)) # 27
print(10 % 3) # 1
my_num = 5
print(str(my_num) + " my favorite number.")  # 5 my favorite number.
# print(my_num + " my favorite number.")  # error
my_num = -5
print(abs(my_num)) # 5
print(pow(3, 6)) # 729
print(max(4, 6)) # 6
print(min(4, 6)) # 4
print(round(3.7)) # 4
print(round(3.7)) # 4
print(round(3.2)) # 3
print(sqrt(36)) # 6

#GETTING INPUT FROM USERS
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello " + name + "! You are " + age)


# BUILDING A BASIC CALCULATOR
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result =  float(num1) + float(num2)

print(result) # Adittion Takes place


# Mad Libs Games
color = input("Enter a color:")
plural_noun = input("Enter a Plural Noun:")
celebrity = input("Enter a Celebrity:")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I Love " + celebrity)
