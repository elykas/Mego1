# def Show (a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c],end=" ")
#         print()   


# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]


# b=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]

# #rotate right
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[c][len(a)-1-r]=a[r][c]
        
# Show(a)
# print()
# Show(b)

# #rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[c][len(a)-1-r]=a[r][c]


# def Ketem(a,v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0]-1)):
#                if(a[r][c]==v):
#                     if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                         return True
#     return False
# a=[
#      [1,2,3,4,5],
#      [3,4,5,9,8],
#      [7,8,3,2,5],
#      [6,1,4,3,2],
#      [5,4,3,2,1]
#      ]
# for i in range(10):
#     print(i,Ketem(a,i)) 

# def KetQty(a):
#     b=[0]*10
#     for r in range(len(a)-1):
#         for c in range (len(a[0])-1):
#              if(a[r][c]==a[r][c+1] and a[r][c]==a[r+1][c] and a[r][c]==a[r+1][c+1]):
#                  b[[a[r][c]]]+=1
#     return b
# a=[
#      [1,2,3,4,5],
#      [3,4,5,9,8],
#      [7,8,3,2,5],
#      [6,1,4,3,2],
#      [5,4,3,2,1]
#      ]
# r=KetQty(a)
# print(r)




#miyun im mone
import random
a=[0]*100
for i in range(len(a)):
    a[i]=random.randint(0,100)
print(a)
counters=[0]*101
for i in range(len(a)):
    counters[a[i]]+=1
print(counters)
index=0
for i in range(0,101,1):
    k=0
    while(k<counters[i]):
        a[index]=i
        index+=1
        k+=1
print()
print(a)

# import random
# a=[0]*1000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# print(a)
# for n in range (0,len(a)-1,1):
#     for b in range (n+1,len(a),1):
#         if(a[b]<a[n]):
#             temp=a[b]
#             a[b]=a[n]
#             a[n]=temp
# print(a)

#maarach ole veyored
# def Pisga(a):
#     i=O
#     while(i<len(a) and a[i]<a[i+1]):
#         i+=1
#     if(i==len(a)-1 or i==0):
#         return -1
#     p=i
#     while(i<len(a) and a[i]>a[i+1]):
#         i+=1
#     if(i==len(a)-1):
#         return p 
#     return -1
# a=[1,2,3,4,3,2,1,0]  
# print(Pisga(a))


# a=[1,2,1,2,5,4,6,7,8,3]
# i=1
# while(i<len(a)-1):
#     if(a[i]>a[i-1] and a[i]>a[i+1]):
#         print(a[i])
#         i+=2
#     else:
#         i+=1
