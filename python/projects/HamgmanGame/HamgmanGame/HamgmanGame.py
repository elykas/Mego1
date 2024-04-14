

#option 1
# max_tries=6
# word=input("Please enter a word: ").lower()
# word = list(word)
# pr=["_"] * len(word)
# print(pr)
# while True:
#     i=0
#     user=input("Please enter a letter:" ).lower()
#     user=list(user)
#     if user[0] in word:
#         while(i<len(word)):
#             if(user[0] == word[i]):
#                 pr[i]=user[0]
#                 i+=1
#             else:
#                   i+=1
#     else:
#         max_tries-=1
#         print("error")
#         print("Your tries left: ", max_tries)    
#     print(pr)
#     if("_" not in pr):
        
#         print("Congratulations!!, You guess the word")
#         break  
#     if max_tries==0:
#         print("Sorry, your max tries run")
#         break
   
    
max_tries = 6
word = input("Please enter a word: ").lower()  # Convert word to lowercase
display_word = "_" * len(word)
print(" ".join(display_word))

while True:
    user_letter = input("Please enter a letter: ").lower()  # Convert input letter to lowercase
    if user_letter in word:
        new_display_word = ""
        for i in range(len(word)):
            if word[i] == user_letter:

                new_display_word += user_letter
            else:
                new_display_word += display_word[i]
        display_word = new_display_word
        print(" ".join(display_word))
    else:
        max_tries -= 1
        print("Error. You have", max_tries, "tries left.")
    
    if "_" not in display_word:
        print("Congratulations! You've guessed the word correctly.")
        break
    
    if max_tries == 0:
        print("Sorry, you've run out of tries. The word was:", word)
        break
    
    

