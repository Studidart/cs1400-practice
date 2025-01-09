i = int(input("Enter a Year: "))
if i % 4 == 0:
    print("its a leap year")
elif i % 400 == 0:
    print("is a leap year")
else:
    print("its not a leap year")