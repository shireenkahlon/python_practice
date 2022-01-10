#This project will ask a user for their name and age. It will then give a message telling the user what year they will turn 100. 
#practice website: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#add dependencies
from datetime import date

#create a current_year variable
current_year = date.today().year

#ask a user for their name and age
name = input("What is your name? ")
age = input("How old are you? ")

#convert the age to an integer
age_int = int(age)

#calculate the year the user will turn 100
age_message = print(name + " will turn 100 in the year ", current_year + (100 - age_int))

#Extra: Ask the user for a number. Print out that many copies of the above message on the same line.

#ask the user for a number
number = input("Give me a number: ")

#convert number to an integer
number_int = int(number)

    
#Extra: print the above message on different lines

#Create a for loop from range number
for i in range(number_int):
    #print the message
    print(name + " will turn 100 in the year " + str(current_year + (100 - age_int)) + "\n")

