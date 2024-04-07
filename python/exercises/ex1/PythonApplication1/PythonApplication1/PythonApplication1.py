


a=1
while (a<7):
    print (" " * (18-a),end=" " )
    b=0
    while(b<a):
        print("*",end= " ")
        b +=1
    a+=1
    print()
 #triangule 2
d=7
e=0
o=0
while(d>1):
    c=1
    k=1
    n=2
    
    print (" " * e,end = " ")
    while(d>c):
        print("*",end=" ")
        c+=1
    
    
    while(n<d):
         print(" ",end=" ")
         n+=1
    
    print(" " * o , end=" ")
    while(k<d):
        print("*",end=" ")
        k+=1
    d-=1
    e = e+1
    o+=4
    print()
    

    #triangule 3
g=1
r=12
while (g<7):
    print(" " * (7-g),end="")#print the first air
    v=1
    s=0
    h=0
    while(h<g):#print the first triangule
        print("* ",end="")
        h +=1
    while(v<r):#print the second air
        print("  ",end="")
        v+=1
    while(s<g):#
        print("* ",end="")
        s+=1
    r-=1
    g+=1
    
    print()
    
#triangule 4
j=7
i=12
while(j>1):
    k=1
    print (" " * i,end = " ")
    while(j>k):
        print("*",end=" ")
        k+=1
    
    i = i+1
    j-=1
    print()





# a=0
# while(a<10):
#     print( " * " + " " * (8-a) + "*" +" "*(a-1))
    
#triangule v   
# a=1
# while(a<10):
#     print(" " * (a) + "*" + " " * ((10-a)*2) + "*" )
#     a=a+1
#     print()
# print(" " * 11 + "* ")



# a=0
# while(a<5):
#     print(" "*(5-a),end="")
#     b=-1
#     while(a>b):
#         print("*",end= " ")
#         b=b+1
#     a= a+1
#     # print()
     
# a=0
# while(a<5):
#     print(" "*(5-a),end="")
#     b=-1
#     while(a>b):
#         print("*",end="")
#         b=b+1
#     a=a+1
#     print()
             


# a=0
# b=23456
# while(a<100000):
#     a = a+b
# while(a<500000):
#     print("*")
#     a= a+b



# a=10
# while(a>0):
#     b= 0
#     while(a>b):
#         print("*",end= " ")
#         b=b+1
#     a=a-1
#     print()
# print("sof")
     

# a=0
# while(a<5):
#     b = 0
#     while(b<5):
#         print ("*",end= " ")
#         b=b+1
#     a=a+1
#     print()

     
     



#loop that give you a triangule with *
# a = 1
# while(a<20):
#     b = 0
#     while(b<a):
#         print("*",end = " ")
#         b= b +1
#     a = a + 1
#     print()
# print("sof")