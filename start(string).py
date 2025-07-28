#qno1. dealing with illegal character to string and their solutions including escape sequences usage
a='my name is "IMAN" i am "20" yrs old ' #the double quotes can be written within single and vise versa but same quotes can't be nested
b="my name is \"Iman\" and i am \"19\" yrs old" # the same nested quotes can be wriiten with help of excape sequence
print(a)
print(b)
#dealing with multiple line string
c="""my name is iman" 
i am 20 yrs old
i am doing python for first time
its my second day of python code
 """ #the multiple line string is done through  triple single or double quote 

# qno2. getting character of string using array method
name="Iman"
print(name[2]) #as iman have index from 0 to 3 you cant get name[4] it will cause error
# using loop
for x in name:
    print(x)

#qno3. lenght of string 
print(len(name))

#qno4. check if string is present (in) text 
txt="my name is iman "
print ("iman" in txt) # if iman is present in string it will return true otherwise false

if "iman" in txt:
    print("yes it is present")

#check if (not in) txt
print("world" not in txt) 

if "world" not in txt:
    print("no world is not present in string")

#qno5. slicing in string
#positive indexing 
X="Hello Ahmed . I am here!"
print(X[2:5]) #index 5 is excluded and character till index 4 will be printed llo
#negative indexing
print(X[-3:-1]) #index -1 will be excluded and character will start from -2 till -3
#mixed indexing
print(X[5:-3]) 

print(X[:4]) #it will write character from start till 3 , 4 will be excluded
print(X[5:]) #the stop is not defined so it will print from index 5 to end 
#qno6. Modification to string
Y="   World Hello!"
#converting to upper case
print(Y.upper())
#converting to lower case
print(Y.lower())
#replacing character
print(Y.replace("H","y"))
#clearing white spaces
print(Y.strip())
#spliting string
print(Y.split())
Y="hello my name is ahmed i am from lahore" #write number in split function the no of parts you want to divide the string 
z=Y.split(" ",8) #as this string has 9 words but 8 commas is required to split them so 8 will be written in split function
print(z)

#qno6. concetenating the string
L="Ali and "
M="Ahmed are friends "
print(L+M) 
# if you are trying  to concetenate a int or string it will create a error
N=8
# print(M+N)

#qno7. here is solution to above problem if you want to add any varable to string you can do it as by "formats"
print(f"Ahmed has {N:} friends.") 
print(f"the price of bucket is {N:.2F} dollars") # using :,2F will create a decimal value with 2 decimal places
