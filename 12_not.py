print(not True)
print(not False)

#and
print("not and")
print("not true and true =>", not (True and True))
print("not true and False =>", not (True and False))
print("not False and True =>", not (False and True))
print("not False and False =>", not (False and False))

stock = input("ingrese el numero de stock => ")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))