import random
import string

great_pass=[]

print("Welcome to the Password Generator!")
length_pass=int (input("Enter the total number of characters in the password:"))
letters_pass= int (input("Enter the number of letters in the password:"))
numbers_pass=int (input("Enter the number of numbers in the password:"))
symbols_pass=int (input("Enter the number of symbols in the password"))

if length_pass !=(letters_pass+numbers_pass+symbols_pass):
     print("Invalid input. The sum of letters, numbers, and symbols                                                      doesn't match the passwor")
else:
      letter=string.ascii_letters
      number=string.digits
      symbols=string.punctuation
      password_chars=(random.choices(letter,k=letters_pass)+
                      random.choices(number,k=numbers_pass)+
                      random.choices(symbols,k=symbols_pass)
                     )
  
      random.shuffle(password_chars)
      password="".join(password_chars)
      print("Generated Password"+password)