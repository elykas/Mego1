#Program that take every odd number and turn it to even number
# a=[357,896,567,235,7]
# i=0
# print(a)
# while(i<len(a)):
#     if(a[i]%2==1):
#         a[i]+=1
#     i+=1
# print(a)



#Program that take all the even numbers and do the sum of them
# a=[4,5,8,7,9,2]
# print(a)
# i=0
# s=0
# while(i<len(a)):
#     if(a[i]%2==0):
#         s+=a[i]
#     i+=1
# print(s)
     



#print the sum of the numbers of every index
# m=[3245,123,98,4587,3,99]
# i=0
# while(i<len(m)):
#     e=0
#     while(m[i]>0):
#         e=e+m[i]%10
#         m[i]=m[i]//10
#     m[i]=e
#     i+=1
# print(m) 

    
    

 

#take the first number of every index
# m=[3245,123,98,4587,3,99]
# i=0
# while(i<len(m)):
#     while(m[i]>9):
#         m[i]=m[i]//10
#     i+=1
# print(m)      
 


# m=[324,123,98,4587,3,99]   
# i=0
# print(m)
# while(i<len(m)):
#     while(m[i]>99):
#         m[i]=m[i]//10
#     i+=1        
# print(m)

#p
# m=[100,123,98,4587,3,99]
# i=0 
# while(i<len(m)):
#     x=int(input("enter a number : "))
#     if((x-10)>m[i] or (x+10)<m[i]):
#         m[i]=x
#     i+=1
# print(m)



#print one minus the after
# m=[324,123,98,4587,3,99]
# i=1
# while(i<len(m)):
#     print(m[i-1]-m[i])
#     i+=1



#print the text with space between the words and take down the words 
# s= "boker tov ely"
# i=0
# while(i<len(s)):
#     if(s[i]!=' '):
#         print(s[i],end=" ")
#     else:
#         print()
#     i+=1
# print()
# print("sof")


#print the number of spaces 
# s="boker tov haver"
# i=0
# c=0
# while(i<len(s)):
#     if(s[i]== ' '):
#         c+=1
#     i+=1
# print("amount of space ", c+1)    


#Check amount of Capital letter
# s="BoKer tOv HavEr"
# i=0
# c=0
# while(i<len(s)):
#     if(ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
#         c+=1
#     i+=1
# print(c)    



#print all letters
# s="BoKer tOv HavEr"
# i=0
# c=0
# while(i<len(s)):
#     if(ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')or \
#        ord(s[i])>=ord('a') and ord(s[i])<=ord('z')):
#          c+=1
#     i+=1
# print(c)    


# s="BoKer tOv HavEr"
# i=0
# c=0
# while(i<len(s)):
#     if(ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')or \
#        ord(s[i])>=ord('a') and ord(s[i])<=ord('z')):
#          c+=1
#     i+=1
# print(c)    


#print what isn't letter
# s="BoKer tOv Ha/////vEr"
# i=0
# c=0
# while(i<len(s)):
#     if(ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
#        c+=1
#     else:
#       if(ord(s[i])>=ord('a') and ord(s[i])>=ord('z')):
#          c+=1
#     i+=1
# print(len(s)-c)    

