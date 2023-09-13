text = "Ella sabe python"
print(text[0]) #imprime la primer letra
print(text[1]) #imprime la 2 letra
# print(text[999]) parametro no encontrado

size = len(text) #para saber la cantidad de caracteres
print('size => ' ,size) #indica la cantidad de caracteres
print(text[size - 1]) #forma larga para saber el ultimo caracter
print(text[-1]) #forma corta de saber el ultimo caracter

# slicing

print(text[0:5]) #de inicio al la letra posicionada en el caracter 5
print(text[10:16]) #del caracter 10 al 16
print(text[:10]) #inicio al 10
print(text[5:-1]) #caracter 5 al ultimo
print(text[5:]) #caracter 5 al ultimo
print(text[:]) #trae todo
print(text[10:16:1]) #del caracter 10 al 16 de a una letra
print(text[10:16:2]) #del caracter 10 al 16 de a 2 letra
print(text[::2]) #todo de a 5 letras