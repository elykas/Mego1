#validation of id
id="23416937"
i=7
t=0
sum=0
while(i>=0):
    if((i%2)!=0):
        t=int(id[i])*2
        if(t>9):
           t=(t%10)+1            
    else:
        t=int(id[i])
    print(t)
    sum+=t
    i-=1
num = (((sum%10)*10)-sum)%10
print("The validation" , num)
#   1 2 1 2 1 2 1 2   
#   2 2 7 4 7 1 7 3
#   2 4 7 8 7 2 7 6



#Program that the even numbers and print it in the place of previous even number
# a=[0,1,2,3,4,5,6,7,8,9]
# t=a[0]
# i=0
# while(i<7):
#     a[i]=a[i+2]
#     i+=2
# a[len(a)-2]=t
# print(a)    
#             [2,1,4,3,6,5,8,7,0,9]

#  0  2  4  6  8 
#  2  2  4  6  8
#  2  4  4  6  8
#  2  4  6  6  8
#  2  4  6  8  8



#Progran that take the even numbers to the next one
# a=[0,1,2,3,4,5,6,7,8,9]
# t=a[len(a)-2]
# i=8
# while(i>0):
#     a[i]=a[i-2]
#     i-=2
# a[0]=t
# print(a)
#            [8,1,0,3,2,5,4,7,6,9]

#                0   2   4   6   8
#                0   2   4   6   6
#                0   2   4   4   6
#                0   2   2   4   6
#                0   0   2   4   6 



#Program that take evry number one step previous
# a=[33,44,66,99,55,55]
# t=a[0]
# i=1
# while(i<len(a)):
#     a[i-1]=a[i]
#     i+=1
# a[len(a)-1]=t
# i=0
# while(i<len(a)):
#     print(a[i])
#     i+=1              





#function that take the biggest nun=mber of the list
# a=[33,66,88,77,55]
# t=a[0]
# i=1
# while(i<5):
#     if(t<a[i]):
#         t=a[i]
#     i+=1
# print("The biggese number is: " + str(t) )    


#Program that display the smallest number
# a=[200,350,654,859,32,2563]
# m=a[0]
# i=1
# while(i<len(a)):
#     if(m>a[i]):
#         m=a[i]
#     i+=1
#     print(m)
# print("The smallest number is: " + str(m))        


#function that reverses the numbers  
# num=67673
# j=0
# while(num>0):
#     j=j*10+num%10
#     num = num//10
# print(j)    