# CRUD create, read, update, delete

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10 # cambia el ultimo valor por 10
print(numbers)

numbers.append(700) # agrega 700 al final de la lista
print(numbers)

numbers.insert(0, 'hola') #en la primer posicion agerga el hola
print(numbers)

numbers.insert(3, 'change') #en la posicion 3 agrega change
print(numbers)

'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''

tasks = ['todo1', 'todo2', 'todo3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo2') #modifica el elemento indicado
new_list[index] = 'todo chaned'
print(new_list)

new_list.remove('todo1') # elimina el elemento indicado
print(new_list)

new_list.pop() #elimina el ultimo por defecto
print(new_list)

new_list.pop(0) #elimina el elemento seleccionado por posicion
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1,2,5,4,7,9]
numbers_a.sort() #orden acendente
print(numbers_a)

string = ['re', 'ab', 'ed']
string.sort() #orden solo dentro del mismo tipo de "objetos"
print(string)

'''
letters.append('G')
letters[0] = 'Z'
letters.pop(2)
letters.reverse()
'''
