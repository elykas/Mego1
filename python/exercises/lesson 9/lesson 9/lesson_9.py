# def cmpString(s1,s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(ord(s1[i]) < ord(s2[i])):
#             return -1
#         else:
#             if(ord(s1[i]) > ord(s2[i])):
#                 return 1
#     if len(s1)==len(s2):
#         return 0
#     else:
#         return len(s1)-len(s2)
    

# #option 2 compqre
# def cmpString(s1,s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if((s1[i]) != (s2[i])):
#             return ord(s1[i]-ord(s2[i])
#     return len(s1)-len(s2)


           
#Miyun migadol lakatan     
# names=["shimon", "yossef","gad","dan","gadi"]
# print(names)

# for i in range(len(names)-1):
#     for j in range (i+1,len(names)):
#         if (cmpString(names[i],names[j])<0):
#             temp=names[j]
#             names[j]=names[i]
#             names[i]=temp
# print(names)



# #Bdika im yesh ot shel mila bemila aheret
# def s1Ins2(s1,s2):
#     if(len(s1)>len(s2)):
#         return False
#     for i in range(len(s1)):
#        for j in range(len(s2)):
#            if(s1[i]==s2[j]):
#                break
#     if(s1[i]!=s2[j]):
#         return False
#     return True
           
# s1="aaa"          
# s2="xbx"               
# print(s1Ins2(s1,s2))   





#get a number of the biggest couple of str in a list and show the couple
# import random
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c],end=" ")
#         print()
# s=""
# for i in range(100):
#     c=chr(random.randint(97,106))
#     s=s+c
# print(s)
# m=[
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     ]
# #m=[[0 for i in range(10)]for y in range(10)]
# for i in range(len(s)-1):
#     sh=ord(s[i]) - 97
#     a=ord(s[i+1]) - 97
#     m[sh][a]+=1
# Show(m)
# rMax=0
# cMax=0
# for r in range(len(m)):
#     for c in range(len(m)):
#         if(m[rMax][cMax]<m[r][c]):
#             rMax=r
#             cMax=c
# print(cMax,rMax)
# print(chr(rMax+97), chr(cMax+97))
   

def copy(s1,s2):
    if len(s1)%(s2)!=0:
        return False
    a=0
    while(a<len(s1)//len(s2)):
           b=0
           while(b<len(s2)):
                if(s1[a*(len(s2))+b]!=s2[b]):
                    return False
                b+=1
           a+=1
    return True

