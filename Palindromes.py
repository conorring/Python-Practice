def palindrome(word):
    for i in range(0,int(len(word)/2)):
        if word[i]!=word[len(word)-i-1]:
            return ""
    return "q"
            
    
           

print("This program will tell you if your word is a palindrome.")
while True:
  user_word=input("Give me a word: ")
  x=palindrome(user_word.lower())
  if x:
       print("Your word is a palindrome")
  else:
       print("Your word is not a palindrome")

  ans=input("Would you like to go again?: ")
  if ans.lower()=="no":
    break
  else:
    continue
input("Press enter to exit.")
   








    
    
    
        
