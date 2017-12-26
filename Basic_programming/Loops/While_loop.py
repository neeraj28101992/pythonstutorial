# =================================For Loop=================================
count = 0
while count < 10:
    print(count)
    count+=1

# else in while loop
# while <condition>:
#  <statement>
# else:     This part will only be called if the loop is not break in between.
#  <statement>
count = 0
while count < 5:
    if count == 7:  
        print("Need to break now")
        break   # if the IF statement is satisfied then it will lead to call of break statement and will miss else part
    print(count)
    count +=1
else:
    print("All ended well")
