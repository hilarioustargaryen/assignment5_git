m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
result=0
for i in range(1,m):
 if n%i==0 and m%i==0:
     result= i
print(result)