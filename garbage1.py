
# def check(s):
#     for i in range(n//2):
#         if s[i]==s[n-1-i]:
#             return True
#     return False
# s='asdfgfdsa'
# n=len(s)
# print(check(s))



# def solve(l,b,c):
#     return (l+b)*c
# print(solve(b=2,l=12,c=3))
# print (solve(12,2,3))


# l1=[12,36,2,23,5,1,4,2,7,98,10]
# l2=[13,64,36,19,8,7,23,45,89,98,34]
# print(set(l1).intersection(set(l2)))
# s1=set(l1).intersection(set(l2))
# print(s1)

# l=[]
# n=len(l1)
# m=len(l2)
# for i in range(n):
#     for j in range(m):
#         if l1[i]==l2[j]:
#             l.append(l1[i])
# print(l)

# for i in l1:
#     if i in l2:
#         l.append(i)
# print(l)

# min=l1[0]
# for i in range(n):
   
#     if(min>l1[i]):
#         min=l1[i]
# print(min)
# min=l1[0]
# for i in range(n):
  
#     if(min<l1[i]):
#         min=l1[i]
# print(min)


# def fib(n):
#     if(n==0 or n==1):
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(10):
#     print(fib(i),end=" ")

# def fib1(n):
#     if(n==0 or n==1):
#         return n
#     else:
#         a=0
#         b=1
#         while(n-2):
#             c=a+b
#             a,b=b,c
#             n-=1
#         return c
# print(fib1(7))


# import sys

# def bsearch(l,lb,ub,key):
#     if(lb<=ub):
#         mid=lb+ub//2
#         if l[mid]==key:
#             return mid
#         elif(l[mid]>key):
#             return bsearch(l,lb,mid-1,key)
#         else:
#             return bsearch(l,mid+1,ub,key)
#     return -1


# l=[1,23,34,56,78,93,112,134,152]
# l.sort()
# key=int(sys.argv[1])

# if bsearch(l,0,len(l)-1,key)==-1:
#     print("search succesfull")
# else:
#     print(f"element found at {bsearch(l,0,len(l)-1,key)}th index")


# from sys import last_type


# from pickle import TRUE


# l=[12,56,73,17,88,10,30,35,64]
# k=[3,4,9,13,15,17,91,14,87,99]

# lst=[j for i in l for j in k if i%j==0]
# list=list(set(i for j in[l,lst]for i in j))

# print(list)


# l=[12,4,2,42,-1,-3,7,53,-53,222,155,-537,37]
# f=list(filter(lambda x:x<0,l))
# print(f)
# print(list(map(lambda x:x*x,l)))


# l=['fhsd','dkdfsa','kjkkuoi','sksf','ifyd','jloef']
# k=list(map(lambda x:x.upper(),l))
# print(k)
# print(list(map(lambda x:x.lower(),k)))


# from functools import reduce


# l=[1,2,3,4,5,6,7,8,9,10,11]
# print(reduce(lambda x,y:x+y,filter(lambda x:x%2==0,l)))

# l=[12,56,73,17,88,10,30,35,64]
# k=[3,4,9,13,15,17,91,14,87,99]
# dt={l:k for l,k  in zip(l,k)}
# print(dt)

# from functools import reduce


# l=[1,2,3,4,5,6,7,8,9,10,11]
# a=[9,8,7,6,5,4,3,2,1]
# x=(reduce(lambda x,y:y if x>y else x,a))
# print(x)


# class A:
#     def p(self):
#         print("this is a")
# class B(A):
#     def q(self):
#         print("this is b")
# class D(A):
#     def s(self):
#         print("this is d")
# x=D()
# y=B()
# x.p()
# y.q()
# y.p()
# x.s()



# def fib(n):
#     if(n==0 or n==1):
#         return n 
#     else:
#         return fib(n-2)+fib(n-1)
# for i in range(10):
#     print(fib(i),end=" ")


# t=(1,2,3,4,5,56,6,7,16)
# print(t)
# from threading import Thread
# import time

# def fun():
#     for i in range(5):
#         time.sleep(1)
#         print("aditya")
# t=threading.thread(target=fun)
# s=time.time()
# t.start()
# d=time.time()
# print(d-s)
# start = time.perf_counter()
# def take_rest():
#     time.sleep(1)
#     print("rest taken for 1 sec")
# t1 = Thread(target=take_rest)
# t2 = Thread(target=take_rest)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# finish = time.perf_counter()
# print(f"Process finished in {int(finish-start)} second(s)")


# class fruit:
#     @staticmethod
#     def find(name,price):
#         print(name,price)
# f=fruit()
# f.find('apple',50)


str=input("enter the string--")
l=list(str)
# print(l)
i=0
while(len(l)>0):
    if(l[i]!=l[i+1]):
        i+=1
    else:
        l.pop(i)
        l.pop(i+1)
        i-=2
print(l)
    





