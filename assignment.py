def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:

# What is printed: 3, 4
# The logic: the add_one function takes the number and adds + 1 to it, so value is increased by 1.
# In the 'for number in' statement, it takes the numbers that are higher than 1 (which are 2 and 3) and the add_one function
# adds + 1 to 2 and 3, which print 3 and 4 at the end.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.

# Your answer: the add_one(2) returns 3.
# return inside the function takes one value (in this case 2) and adds 1 to it
# the print in the loop will add 1 to the numbers in the list, so it will keep adding until all the numbers 
# that satisfy the > 1 condition will be get added to 1.
