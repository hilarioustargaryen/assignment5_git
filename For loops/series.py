First = input()
Step = input()

Sum=0

print("First:",end='')
print("Step:",end='')
for i in range(First,100+1,Step):
 if Sum <= 100:
    Sum += i
    print(i,end=' ') 
print()
print("Sum of series:",Sum)
    