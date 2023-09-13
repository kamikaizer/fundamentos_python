my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla",
  'name': "Martin",
  'last_name': "Matayoshi",
  'age': 36
}

print(my_dict)
print(len(my_dict))

print(my_dict['age']) #si el parametro age no existe se trunca el codigo
print(my_dict.get('age')) #si el parametro no existe imprime none y continua con el codigo

print('avion' in my_dict) #se obtiene True o false
print('barco' in my_dict) #se obtiene True o false
