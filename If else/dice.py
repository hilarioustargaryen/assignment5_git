d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below

if (d1 > 6) or (d1 <= 0) or (d2 > 6) or ( d2 <= 0):
  print ("Invalid input")
else:


  num = (d1+d2)

  if num == 7 or num == 11:
    print("Winner")
  elif num == 2 or num == 3 or num == 12:
    print ("Loser")
  else:
    print (num)