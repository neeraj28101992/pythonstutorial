# =================================For Loop=================================
print("<================================For Loop================================>")

# For Loop to iterate over a list.
prime_no = [3, 5, 7, 11, 13, 29]

for x in prime_no:
    print(x)

# For loop over a specific range [e.g. 1-10, 4-8]
for x in range(10):  # 1. Loop starting from e.g [1,2,3,4,5,6,7,8,9,10]
    print(x)

for x in range(14, 20):  # 1. Loop starting from 2. Loop ending at e.g. [14,15,16,17,18,19]
    print(x)
# Note we can also run the loop in revere direction using -ve numbers e.g. range(42,-12,-7)

for x in range(10, 20, 2):  # 1. Loop starting 2. Loop ending at 3. Skip no of elements e.g [10,12,14,16,18]
    print(x)

# Else in for loop.
# Syntax:
# for <variable> in <sequence>:
#	<statements>
# else:      Here else will only be called of the for loop is not broken using any break statement
#	<statements>

edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break           # Here when the spam is iterated then it will break the for loop
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

# The above for loop will give result like
# >>> Great, delicious ham
# >>> No more spam please!
# >>> Finally, I finished stuffing myself

# If we delete the spam value from the array then the output will be.
# >>> Great, delicious ham
# >>> Great, delicious eggs
# >>> Great, delicious nuts
# >>> I am so glad: No spam!
# >>> Finally, I finished stuffing myself


