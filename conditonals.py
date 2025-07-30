#qno1: checking number is either positive negative or zero
n=int(input("Enter a number:"))
if(n<0):
    print("Number is negative.")
elif(n>0):
    print("Number is positive.")
else:
    print("Number is zero.")
#qno2: if number is even or odd
n=int(input("Enter a number:"))
if(n%2==0):
    print("Number is even.")
else:
    print("Number id odd")
#qno3: checking if character is alphabet or consonats
char=input("Enter a character:")
if(len(char)!=1 or not char.isalpha()):
    print("NOT a valid word entered.")
elif char.lower() in ('a','e','i','o','u'):
        print("WORD is vowel")
else:
        print("Word is consonats") 
#qno4:checking leap year
# year=int(input("Enter a year: "))
if( year%4==0 and year%100!=0 ) or (year%400==0):
       print("Year is leap.")
else:
       print("Year is not leap.")
# qno5:checking if number is perfect square or not
n=int(input("enter a number:"))
sqrt=n**0.5
if(sqrt*sqrt==n):
       print("Perfect square")
else:
       print("Not a perfect square")
#qno6:checking if both strings are same or not
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
if (len(str1)!=len(str2)):
       print("both strings are not equal")
else:
    for i in range(len(str1)):
       same=True
       if str1!=str2:
              same=False
              break
    if same:
     print("Strings are equal.")
    else:
     print("Strings are not equal.")
#qno7: check if number is prime or not
n=int(input("Enter a number:"))
for i in range(2,int((n**0.5)+1)):
    is_prime=True
    if(n%i==0):
     is_prime=False
     break
if is_prime==True:
    print("Number is Prime.")
else:
    print("Number is not Prime.")
