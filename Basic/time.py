secs_str = input("Input seconds: ") # do not change this line
secs_int= int(secs_str)

hours =  (secs_int//3600)

r = (secs_int%3600)

minutes = (r//60)

seconds = (r%60)
print(hours,":",minutes,":",seconds) # do not change this line