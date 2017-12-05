import cmath
def sum_of_num():
    num = int(input("Enter first number"))
    num+=int(input("Enter second number"))
    return num

def find_squr_rt():
    num = int(input("Enter the number"))
    print("Output is : %d"%int(cmath.sqrt(num)))

def area_of_triangle():
    pass

def solve_quadratic_eq():
    pass

def swap_number():
    pass

def gen_random_num():
    pass

def km_to_miles():
    pass

def check_odd_even():
    pass

def largest_num():
    pass

def prime_no_in_between():
    pass

print("This program is contains the below functions:")
try:
    f = open("functionality.txt", "r")
    index =1
    print("0 Exit")
    for lines in f.readlines():
        print (index, lines, end="")  # Here end="" is used to suppress the \n that print function adds
        index +=1
    f.close()
except Exception:
    print("Error faced")

#action =
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