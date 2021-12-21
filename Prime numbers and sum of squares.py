import math
n=int(input("Pick any natural number: "))
while True:
    y=0
    print("These are all the prime numbers less than or equal to",n)
    for i in range(2,n+1):
        if (math.factorial(i-1)+1)%i==0:
           print(i)
           x=i**2
           y+=x
    print("The sum of the squares of these numbers is:",y)
    answer=input("Would you like to go again?(Yes/No): ")
    if answer.lower()=="no":
        break
    else:
        n=int(input("Give me another number: "))

input("\n\nPress enter to exit.")
      


       


