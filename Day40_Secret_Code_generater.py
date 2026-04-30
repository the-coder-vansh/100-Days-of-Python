#secret code language generate 

import random
import string 

r1= "abc"
r2="xyz"

print("----- Welcome to Code Generator -----")
code_decode = input("Type 'code' to encrypt or 'decode' to decrypt: ").lower()
word = input("Enter a word: ")

if code_decode == "code":
      if len(word) < 3:
            # Rule: Reverse the word
            print(f"your code is : {word[::-1]}")
      
      else:
            # Rule: Remove first, add to end, add 3 random chars at start/end
            new_word = word[1:] + word[0]
            final_code = r1+new_word+r2
            print(f"your code is: {final_code}")
elif code_decode == "decode":
      if len(word) < 3:
            # Rule: Reverse the word
            print(f"your code is : {word[::-1]}")
            
      elif (len(word) >= 3 and len(word) < 9) :
            print("......this code is not made by this program...... ")
      else :
            # Rule: Remove 3 chars from start and end
            strip_word = word[3:-3]
            original_word = strip_word[-1] + strip_word[:-1]
            print(f"your word is : {original_word}")
