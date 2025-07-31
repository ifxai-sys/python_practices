#qno1 : creating function for calculating square of n.
n=int(input("Enter a number:"))
def square(n):
    return n*n
print(square(n))
#qno2: function to check if number is odd or even
n=int(input("Enter a number:"))
def check_even(n):
    if n%2==0:
        print("Number is even")
    else:
        print("Number is odd")
check_even(n)
#qno3:Write a function to calculate the area of a circle given its radius.
radius=int(input("Enter the radius:"))
def area_of_circle(radius):
    area=3.14*radius**2
    return area
print(area_of_circle(radius))
#qno4: find the maximum of three values
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
def max(n1,n2,n3):
    max=n1
    if n2>max:
        max=n2
    if n3>max:
        max=n3
    return max
print("the maximum of these numbers is: ",max(n1,n2,n3))
#qno5:Write a function that reverses a string.
s=input("Enter a string:")
def reversing(s):
    reversed=""
    for char in s:
     reversed=char+reversed
    return reversed
print(reversing(s))
#qno 6: returning the fictorial of number
n=int(input("Enter a number:"))
def fictorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n* fictorial(n-1)
print(fictorial(n))
#qno7: Write a function to count vowels in a string.
s=input("Enter a string:")
def vowel_count(s):
    count=0
    for char in s:
        if char.lower() in {'a','e','i','o','u'}:
            count+=1
    return count
print(vowel_count(s))
#qno8 : check if number is palidrome
n=int(input("Enter number:"))
def reverse_n(n):
    r_n=0
    while n!=0:
        digit=n % 10
        r_n = r_n * 10 + digit
        n = n // 10
    return r_n
if n==reverse_n(n):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
    
