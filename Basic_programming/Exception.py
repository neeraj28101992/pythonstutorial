# Exception is an event occurs at the running time of the process, that disrupts the normal flow of the code.
""" Syntax for exception handling
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
"""


try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

# Above code will run perfectly
# O/P: Written content in the file successfully


try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

# O/P Error: can't find file or read data


"""=================================If no exception occurs===================================="""

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

# O/P Written content in the file successfully


# ==================================Try finally claus=========================================
# Finally block will be executed in any case if the try block raise any exception or not

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")

finally:
    print("It will always be printed")

# O/P It will always be printed

# ============================Argument for an exception======================================

"""Syntax:
try:
   You do your operations here;
   ......................
except ExceptionType, Argument:
   You can print value of Argument here...
"""

def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");


# ===================================Raising an exception==============================
# Exception can be raised using "raise" statement
"""Syntax:
raise [Exception [, args [, traceback]]]
"""