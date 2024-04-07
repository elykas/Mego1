# input_file = open(r"C:\Users\user\Documents\Dear Prudence  The Beatles.txt",'r')
# text = input_file.read()
# print(type(input_file))
# print(text)
# text=input_file.readline()#using by loop
# for line in input_file:
#     print(line,end="")
# lycrys=None
# while lycrys != '':
#     lycrys=input_file.readline()
#     print(lycrys,end="")

# input_file = open(r"C:\Users\user\Documents\Dear Prudence  The Beatles.txt",'a')
# input_file.write("ely")
# input_file = open(r"C:\Users\user\Documents\Dear Prudence  The Beatles.txt",'r')
# for line in input_file:
#     print(line,end="")
# input_file.close()

# #example
# FILENAME=r"C:\Users\user\Documents\Dear Prudence  The Beatles.txt"
# with open(FILENAME, 'r') as input_file:
#     for line in input_file:
#         print(line, end="")

# #Copy text from one file to another
# FILE_NAME_1=r"C:\Users\user\Documents\full pythin.txt"
# FILE_NAME_2=r"C:\Users\user\Documents\rek python.txt"
# with open(FILE_NAME_1,'r') as input_file:
#     with open(FILE_NAME_2,'a') as copy_file:
#         for line in input_file:
#             copy_file.write(line)



# import math
# def ShowDeviders(x):
#     sqrtX=int(math.sqrt(x))
#     for i in range(2,sqrtX,1):
#         if(x%i==0):
#             print(i," ",x//i,end=" ")
#     if(sqrtX*sqrtX==x):
#         print(sqrtX)
#     else:
#         i+=1
#         if(x%i==0):
#             print(i,x//i)
#     print()

# num=int(input("Entet a number :"))
# ShowDeviders(num)



# import math
# def IsPrime(x):
#     if(x%2==0):
#         print("no")
#     else:
#         sqrtX=int(math.sqrt(x))+1
#         for i in range(3,sqrtX,2):
#             if(x%i==0):
#                 print("no")
#                 break
#             if(i>=sqrtX):
#                 print("Yes")

# IsPrime(5)



# def F(x):
#     r=o
#     i=1
#     while(i<x):
#         r=r+i
#         i+=1
#     return r

# for i in range(3,8):
#     print(F(i))


# def F(x):
#     r=0
#     i=1
#     while(i<x):
#         if(i%2==0):
#              r=r-i
#              print(i,"+",end=" ")
#     else:
#         r=r+1
#         print(i,"-",end=" ")
#     i+=1
#     if(x%2==0):
#         r=r-x
#     else:
#         r=r+x
#     print()

# def F(x):
#     i=1
#     r=0
#     while(i<x):
#         if(i%2==0):
#             r=r-i
#             print(i,"+",end=" ")
#         else:
#             r=r+i
#             print(i,"-",end=" ")
#         i+=1
#     if(x%2==0):
#         r=r-x
#     else:
#         r=r+x
#     print(x,"=",r)
#     return r  
# F(9)




# def Mul(a,b):
#     r=0
#     while(a>0):
#         r=r+b
#         a-=1
#     return r
# def Hezka(x,y):
#     t=1
#     while(y>0):
#         t=Mul(t,x)
#         y=y-1
# if(Mul(7,3)>Mul(2,8)):
#     print("YYY")
# else:
#     print("nnn")



# def Mul(a,b):
#     r=0
#     while(a>0):
#         r=r+b
#         a-=1
#     return r
# def hezka(x,y):
#     t=1
#     while(y>0):
#         t=Mul(t,x)
#         y=y-1
#     return  t
# print(hezka(3,2))




#e=0
#z=0
# for i in range(40):
#     num = int(input("Enter a number :"))
#     if(num>99 and num<1000):
#         print(num%10+(num//10)%10+num//100)
#     if(num%2==0):
#         z+=1
#     else:
#         e+=num
# print(z)
# print(e)



# num=int(input("Enter a number: "))
# c=0
# z=0
# p=0
# s=0
# while(num!=0):
#     c+=1
#     if(num%2==0):
#         z+=1
#     if(num>0):
#         p+=1
#         s+=num
#     num(input("Enter a number:"))
# print(c)
# print(z)
# print(p/s)




# import random
# i=0
# s=0
# while(i<39):
#     n=random.randint(100,999)
#     if(n%2==0):
#         print(n%10+ (n//10)%10 + n//100) 
#     s=s+n
#     i+=1
# print(s/39)



# array=[None]*10
# array[0]=int(input("please enter first numbers:"))
# array[1]=int(input("please enter second numbers:"))
# for i in range (2,10):
#     if(i%2==0):
#         array[i]=array[i-2]*(array[i-1])
#     else:
#         array[i]=array[i-2]+array[i-1]
    
# print(array)

# #Receiving an array from a user and checking the order of the array
# num=[]
# while True:
#     a=int(input("please enter a number:"))
#     if a == -1:
#         break
#     num.append(a)
# print(num) 

# # Option 1 by all function
# # ascending=all(num[i] <= num[i+1] for i in range (len(num)-1))
# # descending=all(num[i] >= num[i+1] for i in range (len(num)-1))

# # if ascending:
# #     print("The array is sorted in ascending order")
# # elif descending:
# #     print("The array is sorted in descending order")
# # else:
# #     print("The array is not sorted")

# #Option2 
# is_ascending=True
# is_descending=True
# for i in range (len(num)-1):
#     if(num[i]<num[i+1]):
#         is_descending=False
#     elif(num[i]>num[i+1]):
#         is_ascending=False
# if is_ascending:
#     print("The array is sorted in ascending order")
# elif is_descending:
#     print("The array is sorted in descending order")
# else:
#     print("The array is not sorted")
        
#Option 3 by function
# def is_sorted(arr):
#     is_ascending=all(arr[i]< arr[i+1] for i in range(len(arr)-1))
#     is_descending=all(arr[i]>arr[i+1] for i in range(len(arr)-1))
    
#     if is_ascending:
#         return "The array is sorted in ascending order"
#     elif is_descending:
#         return "The array is sorted in descending order"
#     else:
#         return "The array is not sorted"
    
# num=[]
# while True:
#     a=int(input("Please enter a number"))
#     if a==-1:
#         break
#     num.append(a)
#     a=int(input("Please enter a number"))
# print(is_sorted(num))


numbers=[]*6
for i in range(6):
   num=int(input("please enter a number :"))
   numbers.append(num)
print(numbers)

for j in range(6):
   if(numbers[j] == numbers[j])



    
    
    
