# ========================================================Dictionaries===============================================

student_dict = {'Name': 'Amit', 'Uid': 1, 'Contact': 22113, 'Email': "abc@g.com"}

# Printing value of dictionary
print(student_dict['Name'])

# Changing value of dictionary
student_dict['Name'] = 'Aakash'
print(student_dict)


# Adding more element in dictionary
student_dict_copy = [
    {'Name': 'Amit', 'Uid': 1, 'Contact': 22113, 'Email': "abc@g.com"},
    {'Name': 'Abhi', 'Uid': 2, 'Contact': 23211, 'Email': "abhi@g.com"}
]

# printing the element from multiple elements
print(student_dict_copy[0]['Name'])

# Delete the key of dictionary
del student_dict_copy[0]['Email']
print(student_dict_copy)
# [{'Name': 'Amit', 'Uid': 1, 'Contact': 22113}, {'Name': 'Abhi', 'Uid': 2, 'Contact': 23211, 'Email': 'abhi@g.com'}]


# Delete all the elements of dictionary
student_dict.clear()
print(student_dict)

# {}


del student_dict_copy
print(student_dict_copy) # Error since the dictionary is deleted