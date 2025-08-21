#Create a dictionary of 3 friends and their favorite colors. Print each friend’s favorite color.
friends={
    "Taiba":{
        "favourite_color":" White"
    },
    "Iman":{
         "favourite_color":"Black"
    },
    "Isra":{
         "favourite_color":"Pink"
    }

}
for k,v in friends.items():
    print(f"{k}'s favourite color is {v['favourite_color']}")
#Store student names as keys and their marks as values. Print only the names of students who scored more than 50.
Students={
    "Taiba":{
        "marks":80
    },
    "Iman":{
         "marks":40
    },
    "Isra":{
         "marks":67
    }
}
for n,m in Students.items():
     if m['marks']>=50:
          print(f"{n} has marks {m["marks"]} greater than 50.")
#Make a dictionary of fruits with their prices. Ask the user to input a fruit name and print its price.
fruits={
     "apple":{
          "price":250
     },
     "banana":{
          "price":300
     },
     "orange":{
          "price":270
     }

}
fruit_name=input("Enter the fruit name you want to buy. ")
if fruit_name in fruits:
    print(f"price of {fruit_name} is {fruits[fruit_name]['price']} ")
else:
          print("Fruit not available ")
#You have a dictionary of countries and their capitals. Ask the user for a country name and print its capital. If the country is not in the dictionary, print “Not found”.
Countries={
    "Pakistan":{
        "capital":"Lahore"
    },
    "USA":{
          "capital":"New York"
    },
    "England":{
          "capital":"London"
    }
}
country=input("Enter a country : ")
if country in Countries:
      print(f"Capital of {country} is {Countries[country]['capital']}")
else:
      print("Not Found.")
#Create a dictionary of words and their meanings (like a mini-dictionary). Ask the user to enter a word and show its meaning.
Dictionary={
    "Eloquent": "Fluent or persuasive in speaking or writing",
    "Serene": "Calm, peaceful, and untroubled",
    "Benevolent": "Well-meaning and kindly",
    "Resilient": "Able to recover quickly from difficulties",
    "Diligent": "Showing care and effort in work or duties",
    "Harmony": "A pleasing combination of different things",
    "Innovate": "To introduce new ideas or methods",
    "Gratitude": "The quality of being thankful",
    "Optimistic": "Hopeful and confident about the future",
    "Compassion": "Sympathy and concern for the suffering of others"
} 
Word=input("Enter a word: ")
for w,m in Dictionary.items():
      if Word.lower()==w.lower():
            print(f"Meaning of {Word} is {m}")
      
#You are given a dictionary of students and their marks in 3 subjects (nested dictionary). Calculate and print each student’s average marks.
Students={
    "taiba":{
        "maths":78,
        "eng":80,#
        "Phy":75
    },
    "Isra":{
        "maths":79,
        "eng":71,
        "Phy":60
    }, 
    "Iman":{
       "maths":85,
        "eng":79,
        "Phy":65
    },

}
for s,m in Students.items():
    total=sum(m.values())
    average=total/len(m)
    print(f"Average Marks of {s} is {round(average,2)}")
#Write a program that counts the frequency of each character in a string and stores it in a dictionary. Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
string="Hello world"
freq={}
for i in string:
    if i!=" ":
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
print(freq)
#Given a list of dictionaries (each dictionary contains name, age, and city), find the oldest person.
people=[]
person1={
    "name":"Taiba",
    "AGE":19,
    "city":"Okara"
}
person2={
    "name":"Iman",
    "AGE":21,
    "city":"Lahore"
}
person3={
    "name":"Isra",
    "AGE":20,
    "city":"Islamabad"
}
people.append(person1)
people.append(person2)
people.append(person3)
oldest_age=0
oldest_name=""
for person in people:
    if person["AGE"]>oldest_age:
        oldest_age=person["AGE"]
        oldest_name=person["name"]
print(f"{oldest_name} is the oldest person with age of {oldest_age}")
#Create an inventory system: 
#A shop has items with quantities. 
#Write a program to let the user “buy” an item (reduce quantity),
#“add stock” (increase quantity), or “check stock” (print remaining quantity).
Inventory={
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20,
    "Milk": 15,
    "Bread": 10,
    "Eggs": 40,
    "Rice": 25,
    "Sugar": 18
}
def buyitems():
    item=input("Enter a product you want to buy :")
    if item in Inventory:
        if  Inventory[item]>0:
            Inventory[item]-=1
            print(f"{item} bought SuccessFully.")
        else:
            print("Item Out of Stock")
    else:
        print("Product Not available in Shop")

def additems():
    item=input("Enter the item you want to add.")
    qty=int(input("Enter the quantity"))
    if item in Inventory:
        Inventory[item]=+qty
    else:
        Inventory[item]=qty
    print(f"{qty} {item}(s) added to inventory.")
def Quantity_avaiable():
    for i,p in Inventory.items():
        print(f"The Quantity of {i} is {p}")
    
buyitems()
additems()
Quantity_avaiable()
#qno1Create a dictionary of 3 students and their marks.
students={"Ali":80,"Fatima":90,"Ahmed":85}
#qno2Access the value of a key.
print(students["Ahmed"])
# #qno3Add a new key-value pair.
students["taiba"]=56
print(students)
#qno4Update the value of a key.
students.update({"Taiba":79})
print(students)
#qno5Delete a key from the dictionary.
students.pop("Ali")
del students['Ali']
print(students)
#qno6 Loop through all key-value pairs.
for name, marks in students.items():
    print(name,marks)
#qno7Check if a key exists in the dictionary.
if "Fatima" in students:
    print("yes it exists!")
else:
    print("no it doesn't exists!")
#qno8Get all keys and all values separately.
print(list(students.keys()))
print(list(students.values()))
#qno9Merge two dictionaries.
students2={"Isra":78,"Mehroz":92,"Misbah":83,"Fatima":70}
merged={**students2,**students}
print(merged)
#qno10Convert two lists into a dictionary (keys and values).
names=["Iman","Taiba","Isra"]
marks=[80,87,70]
stud=dict(zip(names,marks))
print(students)
#qno12Create a dictionary where keys are numbers 1–5 and values are squares.
squares={x+1:(x+1)**2 for x in range(5)}
print(squares)
#qno13:Write a function that inverts keys and values in a dictionary.
original={1:23,2:12,3:46,4:89}
for k,v in original.items():
     print(f"{v}:{k}")
#qno14Create a nested dictionary representing a student’s profile.
studnts={
    "student1":{
      "name":"Iman",
      "Age":20,
      "program":"BSCS"
      
    },
    "student2":{
        "name":"taiba",
        "Age":19,
        "program":"BDS"
    },
    "student3":{
        "name":"isra",
        "Age":19,
        "program":"Bs biotech"
    },
    "student4":{
        "name":"mehroz",
        "Age":20,
        "program":"Pharm D"
    }
}
print(studnts)
#qno15Find the key with the maximum value.
data={1:90,2:33,3:43,5:110,6:15}
max_value=0
key_values=0
for k,v in data.items():
       if v>max_value:
              max_value=v
              max_key=k
print("Key with maximum value",max_key)
#qno16Remove duplicates from a dictionary by values.
originals={1:45,2:20,3:45,4:98,5:45,6:20}
duplicate={}
seen_value=set()
for k,v in originals.items():
    if v not in seen_value:
        duplicate[k]=v
        seen_value.add(v)
print(duplicate)
    
#qno17Convert a list of tuples into a dictionary.
lists=[(2,4),(5,6),(7,8)]
results=dict(lists)
print(results)


