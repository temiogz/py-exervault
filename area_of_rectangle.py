"""
Instruction: 
Write a python program to take user input as length and breadth and find area of a rectangle.

"""

# this reusable func takes in a l and b value, computes and returns the result
def calculate_area_of_rectangle(len, breadth):
  # area of rectangle = length * breadth
  # then we return the final computation of the l and b to the caller
  return len * breadth


# here we take input from user: L & B and cast it as a float point number
user_provided_length = float(input('enter a length: '))
user_provided_breadth = float(input('enter a breadth: '))

# then we pass in the userinputs as argument to the 'calculateAreaOfRectangle' function
# we invoked the function and calculate A-O-R, store the output in the 'result' variable
result = calculate_area_of_rectangle(user_provided_length, user_provided_breadth)

print("A-O-R: ", result)
