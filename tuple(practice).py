# qno1:Create a tuple with 5 numbers.
# tuple=(3,5,7,8,2)
# print(tuple)
# print(type(tuple))
#qno2:Access the first and last element of a tuple.
#print(tuple[0],tuple[4])
#qno3:Check if "banana" exists in a tuple
# tuple=("apple","cherry","banana","orange")
# if "banana" in tuple:
#     print("Yes the banana is present in tuple")
# else:
#     print("No banana is not present")
#qno4:Convert a list to a tuple.
# list=["apple",1,4,8,"orange"]
# tuple=tuple(list)
# print(tuple)
#qno5:Find the index of an element in a tuple.
# tuple=(3,9,8,4,5)
# index_number=tuple.index(8)
# print(index_number)
#qno6:count the number of element appears
# tuple=(3,6,7,6,7,7,7,8,9,10,10)
# tup=()
# for i in tuple:
#     if i not in tup:
#         count=tuple.count(i)
#         tup+=(i,)
#         print(f"{i} : {count}")
#qno7:slice a tuple from index 2:5
# tuple=(3,9,8,4,5)
# print(tuple[2:5])
#qno8:Unpack a tuple into variables.
# fruits=("Apple","Banana","Orange")
# a,b,c=fruits
# print(a,b,c)
#qno9:Concatenate two tuples.
# fruits=("Apple","Banana","Orange")
# tuple=(3,9,8,4,5)
# tup=fruits+tuple
# print(tup)
#qno10:repeat a tuple 3 times
# repet=("Apple","Banana","Orange")
# repets=repet*3
# print(repets)
#qno11:Convert a tuple of tuples into a flat tuple
# nested_tuple=((2,3),(5,6),(8,3))
# new_tuple=()
# for i in nested_tuple:
#     for j in i:
#         new_tuple+=(j,)
# print(new_tuple)
#qno13:Write a function that returns the second largest number in a tuple.
# def second_max(tup):
#     first=second=float('-inf')
#     for i in tup:
#         if i > first:
#             second=first
#             first=i
#         elif i> second and i!=first:
#             second=i
#     return second
# tuple=(4,6,7,8,9,12,2)
# print("Second Max is :",second_max(tuple))
#qno13:replace an element in the tuple
# t1=(4,6,7,8,9,12,2)
# li=list(t1)
# li[3:5]=9,14
# t2= tuple(li)
# print(t2)
#qno14:use tuple as a key for dict
# ts=("id","name","age")
# dict={ts:"Values"}
# print(dict)
#qno15:Create a tuple from user input.
# tups=()
# for i in range(5):
#     inp=input("Enter the values for tuple:")
#     tups+=(inp,)
# print(tups)
#qno16:Return all elements of a tuple except the first and last.
# ts=(1,7,8,9,4,2)
# print(ts[1:-1])
#qno17:Swap values of two variables using tuple unpacking.
# a=23
# b=34
# print(f"Before swapping a={a} , b={b}")
# a,b=b,a
# print(f"After swapping a={a} , b={b}")
#qno18:Iterate through a tuple and print only strings.
# tups=("Iman",2,5,"Lahore",6,"Pakistan")
# for i in tups:
#     if isinstance(i,str):
#         print(i)
# #qno19:Create a tuple of tuples where each inner tuple contains a number and its square.
# nested_tups=()
# for i in range(5):
#         inp=int(input("Enter a Number: "))
#         sqr=inp**2
#         nested_tups+=((inp,sqr),)
# print(nested_tups)
#qno20:Sort a list of tuples by the second element.
li=[(4,6),(3,2),(8,3)]
for i in range(len(li)):
     for j in range(len(li)-1-i):
          if li[j][1]>li[j+1][1]:
               li[j] , li[j+1]= li[j+1], li[j]
print(li)