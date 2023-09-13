text = "Ella sabe programar en Python"
"""
in busca la palabra en la variable
print("JS" in text)
print("Python" in text)

if "JS" in text:
  print("Elegiste bien)
else
  print("Tambien elegiste bien")
"""

size = len(
  text)  #contabiliza la cantidad de letras y espacios que tiene el texto
print(size)

print(text)
print(text.upper())  #todo el texto a mayuscula
print(text.lower())  #todo el texto a minuscula
print(text.count("a"))  #contaor de letras a en el texto
print(text.swapcase())  #invierte la mayusculas y minusculas
print(
  text.startswith("Ella"))  #true o false palabra con la que comienza el texto
print(
  text.endswith("asdasd"))  #true o false palabra con la que termina el texto
print(text.replace("Python", "Go"))  #remplaza palabra

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())  #pone mayuscula a la primer palabra
print(text_2.title())  #pone mayuscula a la primer letra de cada palabra
print(text_2.isdigit()
      )  # true o false indica si el texto tiene numeros esten en str o int
