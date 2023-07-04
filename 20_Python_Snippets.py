# 20 Python Snippets
# Useful for many problems

####################################
# Author Insta:  @python.science 
####################################

string = "Hello world"
my_list = [1,5,7,9,11,15,8,5,13,8]
my_list2 = []
my_dict = {"apple": 3, "banana": 5, "orange": 2, "pear": 1, "grape": 4}
nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
dict1 = {"apple": 3, "banana": 5}
dict2 = {"orange": 2, "pear": 1, "grape": 4}

# --- Reversing a string ---
print (string)
reversed_string = string[::-1]
print (reversed_string)

# --- Check if a string contain a sub string ---
substring = "world"
if substring in string:
    print ("\nSubstring found!! \n")

# --- Find maximum value in a list ---
max_value = max(my_list)
print ("The max value in the list is: ", max_value)

# --- Find the index of the maximum value of the list ---
max_index = my_list.index(max(my_list))
print ("\nThe index of the max value is:  ", max_index)

# --- Reversing a list ---
reversed_list = my_list[::-1]
print ("\nReversed list:  ", reversed_list)

# --- Removing duplicates from a list ---
my_list_new = list(set(my_list))
print ("\nList ordered and with no duplicates:  ", my_list_new)

# --- Check if a list is empty ---
if not my_list2:
    print ("\nList is empty!!")

# --- Convert a string to a list ---
string_list = list(string)
print ("\nString converted in a list:  ", string_list)

# --- Sort a dictionary by value ---
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print ("\nSorted dictionary by value:  ", sorted_dict)

# --- Check if a file exists ---
import os
if os.path.isfile("20_Python_Snippets.py"):
    print ("\nFile exists!!")

# --- Count occurrences of an item in a list ---
num = 5
count = my_list.count(num)
print ("\nThe number", num, "is:  ", count)

# --- Check if all elements in a list are unique ---
if len(my_list) == len(set(my_list)):
    print ("\nAll elements are unique!!")

# --- Remove all occurrences of an item from a list ---
item = 5
my_list = [x for x in my_list if x != item]
print ("\nList with no", item, "in it:  ", my_list)

# --- Flat a nested list ---
flattened_list = [x for sublist in nested_list for x in sublist]
# print ("\nNested list:  ", nested_list)
print ("\nFlattened list:  ", flattened_list)

# --- Merge two dictionaries ---
merged_dict = {**dict1, **dict2}
print ("\nMerged dictionary:  ", merged_dict)

# --- Remove whitespace from a string ---
string2 = "    hello    world     "
new_string = "".join(string2.split())
print ("\nString with no whitespaces:  ", new_string)

# --- Check if a string is a palindrome ---
pal_string = "racecar"
if pal_string == pal_string[::-1]:
    print ("\nString is a palindrome!!")

# --- Remove duplicates from string ---
remv_string = "".join(set(string))
print ("\nString with no duplicates:  ", remv_string)

# --- Count the number of words in a string ---
word_count = len(string.split())
print ("\nNumber of words in", string, "is:  ", word_count)

# --- Generate a random integer ---
import random
random_number = random.randint(1,100)
print ("\n",random_number)
