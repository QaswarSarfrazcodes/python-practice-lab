#Creating a List
#Accessing List Elements
#Adding Elements to List
#Updating Elements into List
#Removing Elements from the List
#Iterating Over Lists

#Python List Operations
my_list = [0 , 1 ,2 , ' Qaswar', 0.5, 3.14, True, None]
print(my_list)
#Accessing List Elements
print(my_list[3])
#Adding Elements to List
my_list.append('Sarfraz')
my_list.insert(5, 'Ali')
print(my_list)
#Updating Elements into List
my_list[4] = 'Sarfraz'
print(my_list)
#Removing Elements from the List
my_list.pop(5)  # Removes the element at index 5
print(my_list)
#Iterating Over Lists
for items in my_list:
    print(items)