#qno1:creating list of 10 nnumber and printing even of it
numbers=[]
for i in range(11):
     num=int(input("Enter numbers:"))
     numbers.append(num)
 for j in numbers:
     if j%2==0:
         print(j)

#qno2:Find the maximum and minimum element in a list.
 numbers=[]
 for i in range(5):
     num=int(input("Enter numbers:"))
     numbers.append(num)
 max=numbers[0]
 min=numbers[0]
 for j in numbers:
     if j>max:
         max=j
 for j in numbers:
     if j<min:
         min=j
 print("The maximum number is: ",max)
 print("The minimum number is: ",min)

#qno3:Write a program to reverse a list.
 list=[]
 for i in range(5):
     li=input("Enter list element:")
     list.append(li)
 list.reverse()
 print(list)
#qno4:Sort a list in ascending and descending order.
#in ascending order
 list=[1,4,8,34,20,123,345]
 list.sort()
 print("IN ascending order:",list)
 #in descending order
 list.sort(reverse=True)
 print("In descending order:",list)
#qno5:Count how many times a specific element appears in a list.
 li=[1,2,4,2,6,2,7,2,2,2,8,2]
 element=2
 count=0
 for element in li:
     if element==2:
         count+=1
 print("The count of 2 in list is ",count)
#qno6:Add all elements of a list.
 li=[12,15,12,34,65,34,19]
 sum=0
 for i in li:
     sum+=i
 print("the sum of all elements is: ",sum)
#qno7:Remove duplicates from a list.
 li=[1,2,4,2,6,2,7,2,2,2,8,2]
 unique=[]
 for i in li:
     if i not in unique:
         unique.append(i)
 print(unique)
#qno8:Create a new list with only positive numbers from an old list.
 old=[1,-3,8,-12,15,87,-233]
 new=[]
 for i in old:
     if i > 0:
         new.append(i)
 print("the liat of positive numbers are: ",new)
#qno9:Insert an element at a specific index in a list.
 li=[3,9,4,6,12,43,56,67]
 li.insert(3,98) #inserting 98 at 3rd index
 print(li)
#qno10: merging two list without using +
#i am using merge sort algorithm.
def merge(left,right):
    result=[]
    i=j=0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
           result.append(left[i])
           i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge([1,7,45,32,12],[49,23,65,12,97]))
#without sorting it can be done by extend
 a=[8,9,5,34,2]
 b=[6,54,34,65]
 a.extend(b)
 print(a)
