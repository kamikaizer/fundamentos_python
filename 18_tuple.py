numbers = (1, 2, 3, 4)
string = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 =>', numbers[0]) #indica el elemento en la posicion 0
print('-1 =>', numbers[-1]) #indica el elemento en la posicion -1 (ultima)
print(type(numbers))

print(string)
print(type(string))

#las tuplas son listas no modificables

print(string.index('zule')) #indica la posicion de zule
print(string.count('nico')) #indica cuantos elemenotso (nico) hay en la lista

my_list = list(string) #transforma la variable string en lista
print(my_list)
print(type(my_list))

my_list[1] = 'juli' #modifica el elemento en 1 por juli
print(my_list)

my_tuple = tuple(my_list) #transforma my_list en tupla devuelta
print(my_tuple)
print(type(my_tuple))