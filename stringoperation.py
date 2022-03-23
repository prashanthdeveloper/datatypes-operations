#string is a sequence datatype and string is immutable datatype.

#
str1="" # singile qoutes and double qoutes
str2=str()   #str type()
print(type(str2))

# ****************************STRING METHODS************************
# capitalize() method: returns the copy of the given string with first character  capitalized and rest lowercased
s1="prashanth"
s2=s1.capitalize()
print(s2) #output:Prashanth

#lower() method: converts the given string charatcers into lowercase characters and return 
s3="PrAshaNTh"
s4=s3.lower()
print(s4) #output:prashanth

#upper() method: converts the given string charatcers into uppercase characters and return 

s5="prAshaNTh"
s6=s3.upper()
print(s6) #output:PRASHANTH

#swapcase() method: this method converts the given  all string characters into if that character is lower converts into upper and upper into lower
s7="PrograMMIng LanguaGe" 
s8=s7.swapcase()
print(s8)


#casefold() method: this method converts string into lowercase

uname=input("enter uname")
if uname.casefold()=="prashanth":
    print("valid user")



# center() methdo:

s9="prashanth"
s10=s9.center(20,"*")
print(s10)
