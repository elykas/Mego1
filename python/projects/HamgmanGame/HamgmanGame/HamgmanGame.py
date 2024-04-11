


max_tries=6
word=input("Please enter a word: ")
word = list(word)
pr=["_"] * len(word)
print(pr)
while True:
    i=0
    user=input("Please enter a letter:" )
    user=list(user)
    if user[0] in word:
        while(i<len(word)):
            if(user[0] == word[i] and user[0]!= pr[i]):
                pr[i]=user[0]
                break
            else:
                  i+=1
    else:
        max_tries-=1
        print("error")
        print("Your tries left: ", max_tries)    
    print(pr)
    if("_" not in pr):
        print("Congratulations!!, You guess the word")
        break  
    if max_tries==0:
        print("Sorry, your max tries run")
        break
   
    
    
    

