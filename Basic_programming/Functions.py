"""
Rules to define a function:
1. Function block should start with keyword "def" followed by function name and parenthesis {}
2. The code block within every function starts with a colon (:) and is indented.
Syntax:
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
"""

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


"""=============Pass by value and reference============="""
# In python all the parameters are passed by reference i.e. change in the function reflect outside
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append(1)
   print ("1st Values inside the function: ", mylist)
   mylist.append([1, 2, 3, 4]);
   print("2nd Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


"""
Function Arguments:
1. Required arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments
"""

# Required Arguments
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme()

# Keyword arguments
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme( str = "My string")


# Default Argument
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )


# Variable length argument

"""
Syntax
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
"""
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )



# Anonymous Function or Lambda Function
""" These are the functions that are not define using def keyword instead lambda keyword is used.
Syntax:
lambda [arg1 [,arg2,.....argn]]:expression
"""

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))