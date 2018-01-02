# Tuples are same of like list but the difference is that list values can be changed but tuples can't be changed
# In short, Tuple are the immutable python object. Tuples are parenthesis but Lists are square bracket

tup = {1,'two', 3, 'four', 5}
# To define a tuple with single element you should define it as:
tup2 = {6,}     # Here a comma should be written

# Accessing Values of tuple
print(tup)
# print ("Value is",tup[0])

tup_con = tup + tup2
print(tup_con)