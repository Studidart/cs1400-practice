i = int(input("provide price: "))
if i >= 100:
    i=i*.90
    print("your new price is "+str(i))
else:
    print("no discout for you.")
