#This program will create a random password for the user
#Letters are overwhelmingly more likely so I added in some more
#numbers and symbols

characters='''
qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM123456789
012345678901234567890!£$%^&*@?\|<,.>:;{[]}-_)(*+=#~`¬'
'''
num_char=len(characters)

#Good passwords tend to be between 8 and 10 characters

import random as rand

password=[]
for i in range(rand.randint(8,10)):
    password.append(characters[rand.randint(0,num_char-1)])

Password=''
for i in password:
    Password+=str(i)

print('Here is your randomized password\n',Password,sep='')

input('Press enter to exit')



    


