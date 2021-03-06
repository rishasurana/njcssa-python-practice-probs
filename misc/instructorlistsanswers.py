

#######################################################################################
# 1.1
# Loop through this list using a for loop and print all the values.

list1 = [2, 4, 6, 8, 10, 12]

for i in range(len(list1)):
    print(list1[i])


#######################################################################################
# 1.2
# Change all the values in the list to 0 using a for loop and then print the changed
# list.

list1 = ["dog", "cat", True, 1, 5, 0, 2, False, 1.2]

for i in range(len(list1)):
    list1[i] = 0

print(list1)

#######################################################################################
# 1.3
# Divide all the values in the list by 5. Then print the changed list.

list1 = [5, 10, 15, 20, 25, 30, 35, 40]

for i in range(len(list1)):
    list1[i] = list1[i] / 5

print(list1)

#######################################################################################
# 1.4
# Loop through the list and change all values divisible evenly divisible by 3 into 
# "fizz", all values evenly divisible by 5 into "buzz", and all values evenly divisible
# by both into "fizzbuzz"

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

for i in range(len(list1)):
    if list1[i] % 5 == 0 and list1[i] % 3 == 0:
        list1[i] = "fizzbuzz"
    elif list1[i] % 5 == 0:
        list1[i] = "buzz"
    elif list1[i] % 3 == 0:
        list1[i] = "fizz"

print(list1)


#######################################################################################
# 1.5
# Add ten strings to an empty list using a for loop

empty_list = []

for i in range(10):
    empty_list.append("hi")


#######################################################################################
# 1.6
# Add all numbers in the age list that are between 0 and 18 exclusive into the child
# list. Move all numbers greater than 18 into the adult list. Delete the numbers you move.

age_list = [1, 2, 44, 5, 18, 19, 25, 9, 11, 47, 32, 4, 6, 8, 20]
adult_list = []
child_list = []

for i in range(len(age_list)):
    if age_list[i] < 18:
        child_list.append(age_list[i])
        del age_list[i]
    else:
        adult_list.append(age_list[i])
        del age_list[i]

print(age_list)
print(adult_list)
print(child_list)


