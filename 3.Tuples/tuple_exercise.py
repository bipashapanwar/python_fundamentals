family_members=("Father","Mother","Sister1","Sister2","Brother1")
#tuple unpacking
#father,mother,siblings=family_members -- gives error (too many values to unpack)
father,mother,*siblings=family_members 
print(father,mother,siblings) #o/p- Father Mother ['Sister1', 'Sister2', 'Brother1']

fruits=("kiwi","apple","banana",'cherry')
vegetables=('potato',"tomato",'spinach','cabbage')
animal_products=('egg','milk','butter','ghee')
food_products=fruits+vegetables+animal_products
print(food_products)
#o/p - ('kiwi', 'apple', 'banana', 'cherry', 'potato', 'tomato', 'spinach', 'cabbage', 'egg', 'milk', 'butter', 'ghee')

food_products_list=list(food_products)  #tuple to list
print(food_products_list)
#o/p- ['kiwi', 'apple', 'banana', 'cherry', 'potato', 'tomato', 'spinach', 'cabbage', 'egg', 'milk', 'butter', 'ghee']

#slicing
print(fruits[:3]) #o/p- ('kiwi', 'apple', 'banana')
print(food_products_list[-3:]) #o/p- ['milk', 'butter', 'ghee']
del food_products