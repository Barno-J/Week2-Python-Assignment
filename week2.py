#question 1
my_list= []

#question 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#question 3
my_list.insert(1, 15)
print(my_list)

#question 4
another_list= [50, 60,70]
my_list.extend(another_list)
print(my_list)

#question 5
my_list.pop()
print(my_list)

#question 6
my_list.sort()
print(my_list)

#question 7
index_30= my_list.index (30)

print("index of 30:", index_30)