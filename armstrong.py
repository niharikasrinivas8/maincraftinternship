    

num = int(input("Enter a number: "))
power = len(str(num))

result = sum(int(d)**power for d in str(num))

if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")   