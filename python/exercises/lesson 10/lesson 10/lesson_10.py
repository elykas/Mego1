# def Mirror(m):
#     left=0
#     right=len(m)-1
#     while(left<right):
#         ezer=m[left]
#         m[left]=m[right]
#         m[right]=ezer
#         right-=1
#         left+=1
# a=[1,2,3,4,5,6,7]
# Mirror(a)    #[7,6,5,4,3,2,1]



#Zugi bahathala izugi basof
# a=[13,21,30,40,57,62,70,88,77]
# right=len(a)-1
# left=0
# while(left<len(a) and a[left]%2==0):
#     left +=1
    
# if(left<len(a)-1):
#     while(left<right and a[right]%2==1):
#         right-=1
#     while(left<right):
#         if(a[right]%2==0 and a[left]%2==1):
#             ezer=a[left]
#             a[left]=a[right]
#             a[right]=ezer
#             right-=1
#             left+=1
#         else:
#             if(a[right]%2==1):
#                 right-=1
#             else:
#                 if(a[left]%2==0):
#                     left+=1
                    


# #find the biggest in the row
# a=[
#     [1,4,3,6,5,7],
#     [4,3,6,5,7,9],
#     [3,6,5,7,5,1],
#     [9,3,7,5,7,1],
#     [5,3,6,8,7,6],
# ]
# for c in range(len(a[0])):
#     max=a[0][c]
#     for r in range(1,len(a)):
#         if([r][c]>max):
#             max=a[r][c]
#     print(max)
    

#metsiat tsemed 
# a=[
#     [1,4,3,6,5,7],
#     [4,3,6,5,7,9],
#     [3,6,5,7,5,1],
#     [9,3,7,5,7,1],
#     [5,3,6,8,7,6],
# ]
# m=0
# for r in range(len(a)-1):
#     for c in range(len(a[0])-1):
#         if(a[r][c]==a[r][c+1]):
#             m+=1
#         if(a[r][c]==a[r+1][c]):
#             m+=1
#     c+=1
#     if(a[r][c]==a[r+1][c]):
#         m+=1
# for c in range(len(a[0])-1):
#     if(a[len(a)-1][c]==a[len(a)-1][c+1]):
#         m+=1
        


# #metsiat tsemed 2
# a=[
#     [1,4,3,6,5,7],
#     [4,3,6,5,7,9],
#     [3,6,5,7,5,1],
#     [9,3,7,5,7,1],
#     [5,3,6,8,7,6],
# ]
# m=0
# for r in range(len(a)-1):
#     for c in range(len(a[0])-1):
#         if(a[r][c]==a[r][c+1]):
#             m+=1
#         if(a[r][c]==a[r+1][c]):
#             m+=1
# for r in range(len(a)-1):
#     if(a[r][len(a)-1]==a[r+1][len(a)-1]):
#         m+=1
# for c in range(len(a[0])-1):
#     if(a[len(a)-1][c]==a[len(a)-1][c+1]):
#         m+=1
        

import random
a=[0]*100
a[0]=2
for i in range(1,len(a)):
    a[i]=a[i-1]+random.randint(1,6)
print(a)
x=63
low=0
up=len(a)-1
mid=(low+up)//2
while(low<up):
    if(x==a[mid]):
        print(mid)
        break  
    if x > a[mid] :
            low = mid+1
    else:
         up=mid-1
    mid = (low + up) // 2
if x != a[mid]:
      print("-1")
















        