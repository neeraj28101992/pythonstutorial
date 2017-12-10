student_names = []  # Declare the list

student_id = [1112, 2111, 3223, 4432, 5908, 6785]  # Declare and define the list

student_names.append("Aman")  # Appending the value to the list
student_names.append("Babita")
student_names.append("Chintak")
student_names.append("Neeraj")

student_names[1] = "Binny"  # Over riding the old value

print("Aman" in student_names)  # Check if the specific item is in the list
print(student_names)  # to print the values in the list
print(student_id[2])  # print the value of a specific index
print(student_id[-1])  # print the value of last index
print(student_id[-3])  # print the value in reverse direction from last index of list

print(student_id[2:5])  # Here is the memory layout: |0| 1112 |1| 2111 |2| 3223 |3| 4432 |4| 5908 |5| 6785 |6|
# Above from the memory index between 2 and 5 will be printed
