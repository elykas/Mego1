max_tries=6
word=input("Please enter a word: ")
pr="_" * len(word)
print(pr)
user=input("Please enter a letter:" )
while True:
    i=0
    while(i<len(word)):
        if(user == word[i]):
            pr[i] = user
        else:
              i+=1
    print(pr)
            print("Your tries: " + max_tries)
        else:
            max_tries-=1
            print(pr)
            print("Your tries: " + max_tries)
    user=input("Please enter a letter:" )
    
    

