#Strings in python
fruit= "mango"
print(fruit)
len1=len(fruit)
print("Length of fruit string is = ",len1)

#slicing ing string

print(fruit[0:1])
print(fruit[0:2])
print(fruit[0:5])
print(fruit[-1:-3])
print(fruit[-3:-1])

#for loop in strings can be used to print all the characters in a string at once

for characters in fruit:
    print(characters)

#upper() - converts string to upper case

a="Srushti"
b="Hi Welcome   to STring methods Code"
c="SRUSHTI"
d="srushti"
e="Srushti123"
f="Srushti\n"
g=" "


print(a.upper())

#lower() - converts string to lower case

print(b.lower())

#islower() - check if string is lower case and returns true or False

print(a.islower())
print(d.islower())

#isupper() - check if string is upper case and returns true or False

print(a.isupper())
print(c.isupper())

#isalnum() - check if string is contains only A-Z, a-z, 0-9 and returns true or False

print(a.isalnum())
print(e.isalnum())
print(b.isalnum())

#isalnum() - check if string is contains only A-Z, a-z and returns true or False if 0-9 or punctuation

print(a.isalpha())
print(e.isalpha())
print(b.isalpha())

#replace() - replaces a string with another

print("string without changing - ",a)
print("string after change to replacement - ", a.replace(a,b))
print("string after change to replacement2 - ", a.replace("Sru","Mango"))

#split() - splits string at specified instance and returns separated strings

print(e.split(" "))
print(b.split(" "))

#captilaze() - only first character of the string will be capitalized

print("Before capitalization - ", b)
print("After capitalization- ", b.capitalize())

#center() - align string to center

print("Before aligning to center- ", b)
print("After aligning to center- ", b.center(100))

#count()- counts no. of times a given value has occured

print(a.count("s"))
print(b.count("o"))

#endswith() - checks if given string ends with perticular value

print(a.endswith(("i")))
print(a.endswith(("ti")))
print(a.endswith(("Srushti")))

#startswith() - opposite to endswith()

print(a.startswith(("i")))
print(a.startswith(("S")))
print(a.startswith(("Srus")))
print(a.startswith(("Srushti")))

#find() - searches of 1st occurance of a given value, if value is not there return -1
#if value is present, returns its Index

print(b.find("o"))
print(b.find("z"))

#index() - similar to find but if value is not present, it raises an exception

print(a.index("u"))
print(b.index("o"))
#print(a.index("z"))

#isprintable() - return true or false, if all characters or printable or no

print(a.isprintable())
print(f.isprintable())

#isspace() - true only if string contains white spaces

print(a.isspace())
print(b.isspace())
print(g.isspace())

#istitle() - truse if only first letter of each word is captilised

print(b.istitle())
print(a.istitle())

#swapcase() - uppercase are converted to loewr case and vise verse

print(b.swapcase())
print(a.swapcase())

#title()- capitalizes each letter within a string

print(a.title())
print(b.title())






