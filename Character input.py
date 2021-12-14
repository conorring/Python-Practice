#This code asks a user for their name and birth year.
#It will then tell them the year they will turn 100 years old.
#We then ask them how many times we will print their message.

name=input("What is your name:")
birth_year=int(input("What year were you born?:"))
print(name+", you will turn 100 in the year ",birth_year+100,".", sep="")

no_lines=int(input('How many times would you like to print your sentence again?:'))
sentence=name+', you will turn 100 in the year '+str(birth_year+100)+'.\n'
print(no_lines * sentence)

input("Press enter to exit")



