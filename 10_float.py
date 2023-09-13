# x e y float que se calculan en sistema binario para hacer la operacion matematica "decimal" se deben transformar los valores a int
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)


# hace la comparativa trnasformando los valores en string, .2g limita los decimales
y_str = format(y, ".2g")
print(y_str == str(x))

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance) #abs valor absoluto (numeros positivos)
print(abs(x - y))


