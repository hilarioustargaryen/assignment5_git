x_str = input("Input x: ")
x = int(x_str)
# remember to convert to an int

first_three = x//1000# first_three =
last_two = x% 100 # last_two =
middle_two = (x//100)%100# middle_two =
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)