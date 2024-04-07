# #MERGE 2  arrays
# a=[11,33,45,47,53,68,69,74,]
# b=[13,16,19,22,34,41,51]
# c=[0]*(len(a)+len(b))
# idxA=0
# idxB=0
# idxC=0
# while(idxA<len(a) and idxB<len(b)):
#     if(a[idxA]<b[idxB]):
#        c[idxC]=a[idxA]
#        idxA+=1
#     else:
#         c[idxC]=b[idxB]
#         idxB+=1
#     idxC+=1
# while(idxA<len(a)):
#     c[idxC]=a[idxA]
#     idxC+=1
#     idxA+=1
# while(idxB<len(b)):
#     c[idxC]=b[idxB]
#     idxC+=1
#     idxB+=1
# print(c) #[11, 13, 16, 19, 22, 33, 34, 41, 45, 47, 51, 53, 68, 69, 74]





# #qnty of digits on each number
# a=[3411,3653,42352,47,5,1425,12586,14]
# for i in range(0,len(a),1):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)   #[4, 4, 5, 2, 1, 4, 5, 2]





# #oreder the numbers
# a=[4,6,5,1,2,8,9,7,11,55]
# n=0
# while(n<len(a)-1):
#     b=n+1
#     while(b<len(a)):
#         if(a[n]>a[b]):
#             temp=a[n]
#             a[n]=a[b]
#             a[b]=temp
#         b+=1
#     n+=1
# print(a)   #[1, 2, 4, 5, 6, 7, 8, 9, 11, 55]



#Check if it's sorted
# def IsSorted(a):
#    for i in range(len(a)-1):
#       if(a[i]>a[i+1]):
#          return False
#    return True
# arr=[4,6,5,8,7,6,2] 
# print(IsSorted(arr))



           

#Change from string to int
# def StrToInt(s):
#     t=0
#     for i in range(len(s)):
#          t=t*10+(ord(s[i])-48)
#     return t

# n="6234"
# x=StrToInt(n)
# x+=1
# print(x)




#to flip "qwert" to trewq
# def F(s):
#     q=""
#     for i in range(len(s)):
#         q=s[i]+q
#     return q
# e="qwert"
# print(F(e))  #trewq





# #check if is palindrom
# def IsPalindrom(s):
#     left=0
#     right=len(s)-1
#     while(left<right):
#         if(s[left]!= s[right]):
#             return False
#         right-=1
#         left +=1
#     return True
# print(IsPalindrom())
    


# def IsPerfect():
#     for i in range (1,1000):
#         sumDigits=0
#         ezer =i
#         while(ezer>0):
#             sumDigits+=ezer%10
#             ezer//=10
#         if(i%sumDigits==0):
#             print(i)
# IsPerfect()




# t=input("Enter your phone number :")
# c=0
# while (True):
#      c+=1
#      r=True
#      if(len(t)==11 and t[0]=='0' and t[1]=='5' \
#         and ord(t[2])>=ord('0') and ord(t[2])<ord('9')\
#         and t[3]==('-')):
#         for i in range(4,11):
#             if(ord(t[i])>=ord('9') and \
#             ord (t[i])<=ord('0')):
#               r=False
#      else:
#         r=False
#      if(r==False):
#         t=input("Enter your phone number :")
#      else:
#          break
# print(c)
                
  #mahat summer 2023 3   
# def isOrdered(arr):
#     for i in range(len(arr)-1):
#         if(arr[i]%2!=0):
#             if(arr[i+1]%2==0):
#                 return False
            
#     return True  
# arr=[1,3,5,7]
# print(isOrdered(arr))

#find the number max
# def findMax(x):
#     maxValue = x[0]
#     for i in range(len(x)):
#         if(x[i]>maxValue):
#             maxValue=x[i]
   
#     return maxValue
            
# x=[1,2,34,58,698,584,125,478,5698,21,4]
# print(findMax(x))

