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

demo_dict = {"Name": "Neeraj", "L_name": "Khati"}
print(demo_dict)
# O/P {'Name': 'Neeraj', 'L_name': 'Khati'}
demo_dict["m_name"] = "Singh"
print(demo_dict)  # If the key already exists then it will change that value else adds it
# O/P {'Name': 'Neeraj', 'L_name': 'Khati', 'm_name': 'Singh'}

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
# print(student_dict_copy)  Error since the dictionary is deleted


# Dictionary Operations
student_dict = {'Name': 'Amit', 'Uid': 1, 'Contact': 22113, 'Email': "abc@g.com"}

# You can use "in" keyword to check if a key is a part of a dictionary or not
print ("Name" in student_dict)  # True
print ("Names" in student_dict)  # False
print ("Names" not in student_dict)  # True

# Iterate in a dictionary
for item in student_dict:   # Here item will only provide the keys no its values
    print(item)

for i in student_dict:
    print(student_dict[i])