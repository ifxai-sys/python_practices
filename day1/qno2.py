
# #qno2: checking datatype of enter value
# agr koi bi value input() ka through lata hain hum to wo asa a string ati h hma isa convert krna hota h
x=input("Enter Value:")
if x.lower()=="true" or x.lower()=="false":
     real_type=bool
     if x.lower()=="true":
         converted_value="True"
     else:
         converted_value="False"
elif x.isdigit():
         real_type=int
         converted_value=int(x)
else:
     try:
           real_type=float
           converted_value=float(x)
     except:
           real_type=str
           converted_value=x
print("Datatype: ",real_type)
print("Value: ",converted_value)