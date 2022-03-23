# # s1={}
# s1=set()
# print(type(s1))
# s1={1,2,3,4,5}
# l1=[1,2,3,4,4,5,6,7,7]
# print(s1)
# s2=set(l1)
# print(s2)




# # s2={}
# # s1=set()

# # print(type(s2))
# # print(type(s1))


# # add() method: we can add elemenets after creating set
# s3=s1.add(8)
# print(s1)

# #remove() method: remove element from the set ,if ele is not there keyerror raised

# s4=s1.remove(8)
# print(s1)


# #pop() methof: remove and return the element from the set

# s5=s1.pop() # doesn't take any argument
# print(s5)


# # copy() method:returns a shallow copy of the set.

# s6=s1.copy()
# print(s1)
# print(s6)


# # clear() method: doesn't return any value and return None , doesn't take any argument

# s7={1,2,3,4,5}
# s8=s7.clear()
# print(s7) # returbs empty set()
# print(s8) # retrurns None         


# # update() method: updates the set, adding items 
# s11={1,2,3,4,5,11}
# s9={6,7,8}  
# s10=s11.update(s9)
# print(s11)


# # difference()
# s12={1,2,3,4,5,6,7,8,9}
# s13=s11.difference(s12)
# s14=s12.difference(s11) 
# print(s13,s14,sep='\n')


# intersection() method : new set with both sets elements that are common

# set1={1,2,3,4}
# set2={2,3,5,7}
# set3=set1.intersection(set2)
# set4=set2.intersection(set1)
# print(set3)
# print(set4)

# union() method: a new set with all elements that are in both sets

set1={1,2,3,4,6,9}
set2={2,3,5,7,8,10}
set3=set1.union(set2)
print(set3)
