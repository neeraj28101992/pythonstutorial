student_names = []  # Declare the list

student_id = [1112, 2111, 3223, 4432, 5908, 6785]  # Declare and define the list

# =================================Change elements of lists=================================
print("<================================Change elements of lists================================>")
student_names.append("Aman")  # Appending a single  value to the list
student_names.append("Babita")
student_names.append("Chintak")
student_names.append("Neeraj")

#Adding more than 1 element in the list
student_names.extend(["Suraj", "Tarun"])

student_names[1] = "Binny"  # Over riding the old value
print(student_names)
# ==================================================================
print("<================================Printing elements of lists================================>")
print("Aman" in student_names)  # Check if the specific item is in the list
print(student_names)  # to print the values in the list
print(student_id[2])  # print the value of a specific index
print(student_id[-1])  # print the value of last index
print(student_id[-3])  # print the value in reverse direction from last index of list

# =================================List Slicing=================================
print("<================================Slicing of lists================================>")
print(student_id[2:5])  # Here is the memory layout: |0| 1112 |1| 2111 |2| 3223 |3| 4432 |4| 5908 |5| 6785 |6|
# Above from the memory index between 2 and 5 will be printed

# How to assign the new values to the list in a particular range
print(student_id)      # Old list : [1112, 2111, 3223, 4432, 5908, 6785]
student_id[2:5] = [3333,4444,5555]
print(student_id)       # new list : [1112, 2111, 3333, 4444, 5555, 6785]
# ==================================================================

# =================================Deleting or removing in List=================================
print("<================================Deleting from lists================================>")

del student_names[5]
print(student_names)

del student_names[3:4]
print(student_names)
student_names.pop(1)    # if you want to delete a specific index
student_names.pop()     # if you want to delete the last index
print(student_names)
# del student_names     if you will use this then whole list will be deleted and if you try to print it then you will face error
# student_names.clear() if you use this then all the element of the list will be deleted
# If you want to delete the element from the list by name then use remove function

student_names.remove("Aman")
print(student_names)


# ==================================================================

# =================================List comprehension =================================
# List comprehension is a way to create a list using some pattern e.g. list = [1,2,4,9,16] square of numbers in incrementing order
print("<================================List comprehension ================================>")
pow1_list = [2 ** x for x in range(10)] # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow1_list)

pow2_list = [2 ** x for x in range(10) if x > 5] # Output: [64, 128, 256, 512]
print(pow2_list)
# ==================================================================