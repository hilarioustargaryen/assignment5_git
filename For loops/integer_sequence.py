num = 1
sum = 0
even = 0
odd = 0
largest = 0
loops = False

while (num > 0):
    num = int(input("Enter an integer: "))
    sum = sum+num
    
    if (num <= 0):
        break
    
    if (num % 2) == 0:
        even += 1
    else:
        odd += 1
    if (num >= largest):
       largest = num
    
    loops = True    
    print("Cumulative total:" ,sum)
    
if loops:
    print("Largest number:" ,largest)
    print("Count of even numbers:" ,even)
    print("Count of odd numbers:" ,odd)
