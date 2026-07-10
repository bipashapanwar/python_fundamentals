ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max=ages[-1]
min=ages[0]
ages.append(max)
ages.append(min)
range=max-min
print("Range:",range)
average_age=sum(ages)/2
print(average_age)
print(abs(max-average_age))