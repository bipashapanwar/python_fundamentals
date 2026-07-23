#Tuples are ordered, indexed and immutable
tup1=('bipasha','manvi','kanha','bhagyashree','gautam','manvi') 
#it cannot be modified, but can be accessed using indexes

print(len(tup1))   #o/p- 6
print(tup1.count('bp'))  #o/p- 0
print(tup1.count('manvi'))  #o/p- 2
print(tup1[:3])  #o/p- ('bipasha', 'manvi', 'kanha')
print('bp' in tup1)  #o/p- False
print('kanha' in tup1)  #o/p- True


#tuple to list
lst1=list(tup1)
print(lst1)  #o/p- ['bipasha', 'manvi', 'kanha', 'bhagyashree', 'gautam', 'manvi']
print(tup1)  #o/p- ('bipasha', 'manvi', 'kanha', 'bhagyashree', 'gautam', 'manvi')

#joining two tuples
fruits=('kiwi','apple','mango','berry')
colors=('green','red','yellow','blue')
fruits_and_colors=fruits + colors
print(fruits_and_colors)  #o/p- ('kiwi', 'apple', 'mango', 'berry', 'green', 'red', 'yellow', 'blue')


#checking an item in a tuple
print('green' in colors)  #o/p- True

#individual items cant be deleted, but the whole tuple can be
del tup1
#print(tup1) - gives NameError

