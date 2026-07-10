#1.String concatenation
a="Python"
b='is'
c="AweSOme"
d="Coding for all"
print(a+" "+b+" "+c)             #o/p-Python is awesome

#2.String methods
print(len(a))                    #o/p-  6                                 
print(type(b))                   #o/p- <class 'str'>
print(a.upper())                 #o/p- PYTHON
print("Strings are immutable so a remains as: ",a) #o/p- Python
print(a.lower())                 #o/p- python
print(b.capitalize())            #o/p- Is
print(c.swapcase())              #o/p- aWEsoME
print(d.replace("Coding","Python")) #o/p- Python for all
print(c.count('o'))              #o/p- 0 because case sensitive
print(d.endswith('ll'))          #o/p- True
print(d.isalnum())               #o/p- False bcs space is not alnum
print(a.isalnum())               #o/p- True
print(b.isalpha())               #o/p- True
print(d.title())                 #o/p- Coding For All

company='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(company.split(','))       #splits into a ist of substrings
print(company.index('A'))       #o/p- 29 bcs case sensitive, ValueError if not found
print(company.find('Z'))        #index of first occurence, gives -1 if not found
print(company.rfind('A'))       #index of last occurence, gives -1 if not found

fruits=['apple','mango','banana','kiwi']
print(' '.join(fruits))         #o/p- apple mango banana kiwi




