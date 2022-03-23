### Dict Operations ###

# dictionary get() method : takes 2 arguments  
d1={1:"prashanth",2:"ramcharan"}
print(d1)
print(d1.keys())
print(type(d1.keys()))
print(d1.values())
print(d1.get(3)) # if there is key return  value of key and key is not there return None 
print("**********************")

print(d1.get(5,"Not specified"))

print("**********************")
print(d1[2])        #if there is key return  value of key and key is not there key error raised 
#print(d1[3]) key error
#print(d1.get(6))  #None
print(type(dict))









# dictionary copy() method: doesn't take any argument as parameter

d1={1:"prashanth",2:"sai",3:"ram"}
d2=d1.copy()                #returns shallow copy of the dictionary   
print(d1,d2,sep='\n')

# dictionary clear() method:  doesn't take any argument as parameter
d3={1:"prashanth",2:"sai",3:"ram"}
d=d3.clear()                #
print(d3)

#inserting  key and values into dictionary

d4={}
d4[1]="python"
d4[2]="java"
d4[3]="css"
print(d4)


# dictionary formkeys() method: take 2 arguments 
#  
# syntax  dictionary.fromkeys(sequence[, value])
keys={'a','b','c','d'}
values="alphabets"
d6=dict.fromkeys(keys,values)
print(d6)



# pop() method: takes one argument that is dictionary key
# popitem() method: doesn't take any parameters.

d7={1:"ubuntu",2:"windows",3:"linux"}
d8=d7.pop(1)  #takes parameter as key 
d9=d7.popitem()  # last insertion deleted and returns key value pair
print(d8)
print(d9)
print(d7)



# update() method: updates the dictionary with the new key and value(dictionary object)


d10={1:"ubuntu",2:"windows",3:"linux"}
d11={4:"monitor"}
d12=d10.update(d11)
print(d10)




test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}


print("The dictionary before deletion : ",test_dict)


pop_ele = test_dict.pop('sai',"key not found!")

pop_ele1= test_dict.pop("Akash","key not found!")

print("Value associated to poppped key is : ",pop_ele)

print("Value associated to poppped key is : ",pop_ele1)


print("Dictionary after deletion is : " ,test_dict)








dict1={"name":"prashanth","age":21,"Rol":101}
dict2=dict1["group"]="mstcs"
print(dict1)
print(dict1.keys())
print(dict1.values())
print(type(dict1.values()))
print(dict1.get("name","Key Not Found!"))
print(dict1.popitem())
print(dict1.pop("Rol"))
print(dict1)
dict3={"Rol":101,"Group":"Mstcs"}
dict4=dict1.update(dict3)
print(dict1)

dict1={"name":"prashanth","age":21}
dict3=dict1.update(roll=101,Group="Mstcs")
# dict4=dict1.update(dict3)
print(dict1)
