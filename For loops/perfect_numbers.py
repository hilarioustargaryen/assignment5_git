top_num = int(input("Upper number for the range: ")) # Do not change this line


for i in range(1,top_num):
  result=0
  for j in range(1, i):
    if(i % j == 0):
        result = result + j
  if result == i:
    print(result)
    
