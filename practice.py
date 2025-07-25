#qno1 reversing a string
X="hello"
print(X[::-1]) # is ma hum [start: stop: step ] use kr rha hain start stop ni pta hma wo by default ho ga jab ka -1 at step bta rha h reverse move kro 
#age -1 ki jga -2 hota to ya reverse move krta lakin ak digit skip kr data like "olh" output hota 
#qno2 checking palindrome
X="121"
Y=X[::-1]
if Y==X:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")
#qno3 count vowel 
Alphabets="my name is ali "
count=0
for x in Alphabets:
    if x in'aeiou':
        count+=1
print(count)
#qno4 removing all the spaces
A="hello my name is iman!"
print(A.replace(" ",""))
#qno5 finding lenght of string without using len()
# B=input("enter a string")
# lenght=0
# for x in B: 
#     lenght+=1
# print("the lenght of string is: ",lenght)
#qno6 replacing all vowels with *
Vowels="Aecioisjz"
for x in Vowels:
    if x in 'aeiouAEIOU':
       Vowels=(Vowels.replace(x,'*'))
print(Vowels)
#qno7 making the first letter of each letter in string capital 
string="hello world"
words=string.split()
result=""
for x in words:
    result+=x[0].upper()+ x[1:]+" "
print(result)
#qno8 checking 2 strings are anagrams or not
str1=input("enter string 1:")
str2=input("enter string 2:")
str1=str1.lower()
str2=str2.lower()
if sorted(str1) == sorted(str2):
    print("the both strings are anagrams")
else:
      print("the both strings are not anagrams")
