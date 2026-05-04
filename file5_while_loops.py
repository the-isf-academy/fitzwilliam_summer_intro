# /////////// INSTRUCTIONS /////////////////
# 💻 Run this file 
#      - what is printed out and why?
    
# 💡 while loops, loop until a condition is True (ust like if statements) 
# You can use operators to compare values or to generate True or False conditions.

# 💻 Experiment with changing the numbers in the while loop condition. 
# Then run your code to see how your changes affect what it prints.

# Go to file6.py when you are finished!
# ////////////////////////////////////////////


user_input = -1
while user_input < 1 or user_input > 10:
    user_input = int(input("Tell me a number between 1-10 (inclusive): "))
