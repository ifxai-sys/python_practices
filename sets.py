# #qno1:Create a set of 5 integers.
# integers={4,6,7,8,3}
# print(integers)
# #qno2:Add an element to a set.
# integers.add(12)
# print(integers)
# #qno3:Remove an element from a set.
# integers.remove(6)
# print(integers)
# #qno4:Check if an element exists in the set.
# if 8 in integers:
#     print("8 is present in the set")
# else:
#     print("Not present in set")
# #qno5:Convert a list to a set.
# lists=[4,"Iman",5,5,4,9,6,"Fatima"]
# sets=set(lists)
# print(sets)
# #qno6:Find union of two sets.
# set1={4,5,7,6,2}
# set2={'A',4,5,'C',12,17}
# set3=set1|set2
# print(set3)
# #qno7:Find intersection of two sets.
# set1={4,5,7,6,2}
# set2={'A',4,5,'C',12,17}
# set3=set1&set2
# print(set3)
# #qno8:Find difference between two sets.
# set1={4,5,7,6,2}
# set2={'A',4,5,'C',12,17}
# set3=set1-set2
# print(set3)
# #qno9:Check if one set is a subset of another.
# sets1={1,2,3,4}
# sets2={3,4,5,6,1,2,8}
# print("Is the set1 is subset of set2? ",sets1.issubset(sets2))
# #qno10:Remove all duplicates from a list using a set.
# lists=[4,"Iman",5,5,6,6,6,9,10,11,11,4,9,6,"Fatima"]
# sets=set(lists)
# print(sets)
# #qno11:Find all unique characters in a string.
# string="Iman Fatima"
# sets=set()
# for i in string:
#     if i !=" ":
#         sets.update(i)
# print(sets)
# #qno12:Write a function to return common elements in multiple sets.
# def common(set1,set2,set3):
#     myset=set1&set2&set3
#     return myset
# set1={3,4,5,6,71,12}
# set2={4,5,6,13,18,19}
# set3={5,6,4,71,18,19,12}
# print("the common elements are ",common(set1,set2,set3))
# #qno13:Generate a set of even numbers from 1 to 20.
# even=set()
# for i in range(21):
#      if i!=0 and i % 2==0:
#          even.add(i)
# print(even)
# #qno14:Find symmetric difference between two sets.
# set1={3,4,5,6,71,12}
# set2={4,5,6,13,18,19}
# myset=set1^set2
# print(myset)
# #qno15:Write a program to detect duplicate elements in a list using sets.
# lists=[4,"Iman",5,5,6,6,6,9,10,11,11,4,9,6,"Fatima"]
# seen=set()
# duplicates=set()
# for i in lists:
#     if i not in sets:
#         sets.add(i)
#     else:
#         duplicates.add(i)
# print("Duplicates are",duplicates)
# #qno16:Given two sets, determine if they are disjoint.
# set1={1,2,3,4}
# set2={5,6,13,18,19}
# print("Is set1 and set2 are disjoints? ", set1.isdisjoint(set2))
# #qno17:Find elements present in exactly one of the three sets.
# set1={3,4,5,6,71,12}
# set2={4,5,6,13,18,19}
# set3={5,6,4,71,18,19,12}
# sets1=set1-set2-set3
# sets2=set2-set1-set3
# sets3=set3-set2-set1
# results=sets1|sets2|sets3
# print("Set1 : " ,sets1)
# print("Set2 : " ,sets2)
# print("Set3 : " ,sets3)
# print("Exactly one of three sets are: ",results)
#qno18:Use a set to store prime numbers from 1 to 50.
import math
prime=set()
for i in range(2,51):
    Isprime=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            Isprime=False
            break
    if Isprime:
     prime.add(i)
print(prime)
#qno19:Write a program to check if two lists have any common element using set intersection.
X=[4,5,6,7,8]
Y=[4,5,1,2,7,9]
Z=set(X) & set(Y)
if Z:
   print("Common elements : ", Z)
else:
   print("No common elements :")
#q20:Implement a set operation manually (e.g., union without using | operator).
A={3,4,6,8,9}
B={5,4,3,2,1}
A.update(B)
print(A)