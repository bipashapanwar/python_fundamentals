#1.list unpacking
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)              #o/p- Germany
print(fr)              #o/p- France
print(bg)              #o/p- Belgium
print(sw)              #o/p- Sweden
print(scandic)         #o/p- ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)              #o/p- Estonia

#2.List slicing
print(countries[:4])   #o/p- ['Germany', 'France', 'Belgium', 'Sweden']   [start:stop]
print(countries[1:6:2]) #o/p- ['France', 'Sweden', 'Finland']

#3.mutability
countries[0]="India"
print(countries)

#4.checking items using 'in'
print('France' in countries)   #o/p- True