def sum_of_num():
    num = int(input("Enter first number"))
    num+=int(input("Enter second number"))
    return num

def find_squr_rt():
    pass

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

action = input("\nEnter you choice")
while action != 0:
    if(action == 1):
        print(sum_of_num())
    elif(action == 2):
        find_squr_rt()