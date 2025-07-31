# #qno1: printing even numbers between 1 to 100

# for x in range(1,101):
#     if(x%2==0):
#         print(x ," ")
 
# #qno2: sum of first 50 natural numbers using while loop
# n=1
# sum=0
# while n<=50:
#      sum+=n
#      n+=1
# print(sum)

# #qno3: print the table of the number entered by user
# m=0
# n=int(input("Enter a number: "))
# for m in range (11):
#     print(f"{n} x {m} = {n*m}")

#qno4: find maximum
# n1= int(input("Enter number 1: "))
# n2= int(input("Enter number 2: "))
# n3= int(input("enter number 3: "))
# max=n1
# if n2>max:
#     max=n2
# if n3>max:
#     max=n3
# print(f"{max} is greater")

#qno6: printing the fabonacci series:
# num= int(input("enter a number: "))
# n1=0
# n2=1
# for x in range(num):
#     print(n1)
#     n1,n2=n2,n1+n2

#qno7:counting the number of digits in number entered by user
# n= int(input("enter number: "))
# count=0
# if n==0:
#     count=1
# else:
#     while (n!=0):
#         n = n // 10
#         count+=1
# print(count)
#qno8 : pattern printing
for i in range(1,5):
    for j in range(i):
        print("*", end="") # end remove the newline or spacs 
    print()
#qno9 
for i in range (1,5):
    for j in range (1,i+1):
        print(j , end="")
    print()
#qn10 
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#qno11:
for i in range(1,5):
    for j in range(i):
        print(i , end="")
    print()
#qno12:
for i in range(4,0,-1):
    for j in range(i):
        print(i, end="")
    print()
#qno13:finding factorial 
# fact=1
# n=int(input("Enter a number:"))
# if n==0 or n==1:
#   fact=1
# else:
#     for i in range(n,1,-1):
#         fact=fact*i
# print(fact)
#qno14: reversing a number using loops 
# n=int(input("Enter a number:"))
# r_n=0
# while n>0:
#      digit=n%10
#      r_n=r_n*10+digit
#      n=n // 10
# print("reversed number: ", r_n)
#qno15:prime numbers between 1 and 50
import math
for i in range(2,50):
    is_prime=True
    for j in range (2,int(math.sqrt(i))+1):
        if i%j==0:
            is_prime=False
            break
        else:
            is_prime=True
    if(is_prime==True):
      print(i)
        
    

