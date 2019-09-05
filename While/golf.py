par = int(input("Par of hole 1:"))
score = int(input("Score on hole 1:"))
i= 1
while i< 18:
    
  if par < 3:
       print("invalid score")
  if (par - score) == 3:
       print("albatross")
  if (par - score) == 2:
       print("eagle")
  if (par - score) == 1:
       print("birdie")
  if (par - score) == 0:
       print("par")
  if (par - score) == -1:
       print("bogey")
  if (par - score) == -2:
       print("double bogey")
  if (par - score) == -3:
       print("triple bogey")
  elif (score - par) >= 4:
       print("bad hole")
  par = int(input("Par of hole " + repr(i+1) + ":"))
  score = int(input("Score on hole " +repr(i+1) + ":"))
  i += 1