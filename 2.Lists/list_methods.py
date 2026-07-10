fruits=['banana','kiwi','orange','mango','litchi']
fruits.append('apple')      #apple is added to the end of list       
fruits.insert(2,'melon')    #(index,item) 
print(fruits) 
print(len(fruits))
fruits.remove('melon')      #removes specified item


#it refers to the same list, changing one will change the other
fruits1=fruits
fruits1[0]='India'
print(fruits)
  
#if you want to make a copy instead, use copy()
fruits2=fruits.copy()
print(fruits2)

fruits.pop()                #removes last element by default
fruits.pop(2)               #removes specified index
del fruits[3]               #removes specified index
del fruits[0:2]             #deletes sliced elements
print(fruits)
fruits.clear()              #clears the whole list but doesnt delete the structure
del fruits                  #deletes the whole list
#print(fruits)              #will give NameError

#List Concatenation and Joining
#using +
list1=[1,2,3,4,5]
list2=[6,7,8,9]
list3=list1+list2
print(list3)

#using extend()
list1.extend(list2)    #doesnt need a new list, modifies list1
print(list1)

list1.reverse()
print(list1)

#sorting lists
num=[43,53,2,44,55,48,5]
num.sort()    #modifies the list itself in ascending order
print(num)
num.sort(reverse=True)  #in descending order
print(num)
num1=[4,34,2,4,5,664,37]  
print(sorted(num1))  #doesnt modify original list
print(num)





