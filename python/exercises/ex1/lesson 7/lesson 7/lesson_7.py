#qty of the numbers of the list
# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2]
#     ]
# for r in range (len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         print(a[r][c],end=" ")
#         sum+=a[r][c]
#     print("   ", sum)  
        

#get the biggest number of each list
# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2]
#     ]       
# for r in range (len(a)):
#     max=0
#     for c in range(len(a[r])):
#         print(a[r][c],end=" ")
#         if(max<a[r][c]):
#             max=a[r][c]
#     print("   ", max)  
        
    

#print the row in the column
# a=[
#     [1,2,3,4,5],
#     [2,3,4,5,9],
#     [9,8,7,6,5],
#     [8,7,6,5,0],
#     [3,4,5,9,8],
# ]
# for c in range(len(a[0])):
#     for r in range(len(a)):
#         print (a[r][c],end=" ")
#     print()
        

#multiplication of 2 lists option 1
# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# for i in range(len(a)):
#     for k in range(len(b)):
#         c[i]=c[i]+a[i]*b[k]
# print(c) 


#multiplication of 2 lists option 2
# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# sumB=0
# for i in range(len(b)):
#     sumB+=b[i]
# for i in range(len(a)):
#         c[i]=a[i]*sumB
# print(c) 




# left=[
#     [2,5,4,6],    
#     [9,3,1,4],    
# ]
# right=[
#     [4,7,9],    
#     [1,2,3],    
#     [9,6,7],    
#     [3,2,3],    
# ]
# m=[
#     [0,0,0],
#     [0,0,0],
#   ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         for i in range(len(left[0])):
#             m[r][c]=m[r][c]+left[r][i]*right[i][c]
# print(m)            



# import random
# letters=['a','b','c','d','e','f','g','h','i','j',
#          'k','l','m','n','o','p','q','r','s','t','u',
#          'v','w','x','z']
# hatspan=['a','b','c','d','e','f','g','h','i','j',
#          'k','l','m','n','o','p','q','r','s','t','u',
#          'v','w','x','z']
# swapCount=random.randint(22,66)
# for i in range(swapCount):
#     idx1=random.randint(0,len(letters)-1)
#     idx2=random.randint(0,len(letters)-1)
#     ezer=hatspan[idx1]
#     hatspan[idx1]=hatspan[idx2]
#     hatspan[idx2]=ezer
# text="boker tov"
# newText=[" "]*len(text)
# for i in range(len(text)):
#     idx=ord(text[i])-ord('a')
#     newText[i]=hatspan[idx]
# print(newText)




# #mahat 2023
# a= int(input("Please enter a number :"))
# max=num
# min=num
# while(num<100 or num>999):
#         if(a>max):
#             max=a
#         elif(min>a):
#             min=a
#         a= int(input("Please enter a number :"))
# if(a>max):
#     max=a
# elif(min>a):
#     min=a
# print(min,max)                
 
import math
def ThePrimers(x):
    num=1
    while(num<=x):
        if num%2!=0:
           sqrtx=int(math.sqrt(num) +1)
           for i in range(3,sqrtx,2):
               if num%i==0:
                   break
           if i == sqrtx:
               print(1,2,num)
x=20
ThePrimers(x)
        



