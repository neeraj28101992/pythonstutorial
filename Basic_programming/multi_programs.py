import cmath
import random

def sum_of_num():
    num = int(input("Enter first number"))
    num += int(input("Enter second number"))
    return num


def find_squr_rt():
    num = int(input("Enter the number"))
    print("Output is : %f" % num ** .5)


def area_of_triangle():
    num_1 = int(input("Enter the first number: "))


def solve_quadratic_eq():
    pass


def swap_number():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    print("Before swap: ", num_1, num_2)
    num_1 = num_1+num_2
    num_2 = num_1 - num_2
    num_1 = num_1 - num_2
    print("After swap: ", num_1, num_2)


def gen_random_num():
    print("Random number generated is ; ",random.randint(1,100))


def km_to_miles():
    num = int(input("Enter the distance in KM"))
    print(num,"Km = ",num*0.621371, "Miles")


def check_odd_even():
    num = int(input("Enter the number:"))
    print("even") if num % 2 == 0 else print("odd")
    pass


def largest_num():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the third number:"))

    if num1 > num2 and num1 > num3:
        print(num1, " is biggest")
    elif num2 > num3:
        print(num2, " is biggest")
    else:
        print(num3, " is biggest")
    pass


def prime_no_in_between():
    num1 = int(input("Enter the starting range:"))
    num2 = int(input("Enter the ending range:"))
    for num1 in num2:
        count = 0
        for j in num1:
            if num1 % j == 0:
                count+=1

        if count <= 0:
            print(num1)




print("This program is contains the below functions:")
try:
    f = open("functionality.txt", "r")
    index = 1
    print("0 Exit")
    for lines in f.readlines():
        print(index, lines, end="")  # Here end="" is used to suppress the \n that print function adds
        index += 1
    f.close()
except Exception:
    print("Error faced")

# action =
while True:
    action = int(input("\nEnter you choice"))
    if action == 0:
        break
    elif action == 1:
        print(sum_of_num())
    elif action == 2:
        find_squr_rt()
    elif action == 3:
        area_of_triangle()
    elif action == 4:
        solve_quadratic_eq()
    elif action == 5:
        swap_number()
    elif action == 6:
        gen_random_num()
    elif action == 7:
        km_to_miles()
    elif action == 8:
        check_odd_even()
    elif action == 9:
        largest_num()
    elif action == 10:
        prime_no_in_between()
    else:
        print("Wrong choice mate")
