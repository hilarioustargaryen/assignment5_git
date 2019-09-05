num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
odd=1
curr=1
while odd <= num:
  if  curr % 2 == 1:
    print (curr)
    odd += 1
  curr += 1