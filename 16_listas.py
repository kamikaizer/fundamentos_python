numbers = [1,2,3,4]
print(type(numbers))
print(numbers)

task = ['make a dishes', 'play videogames']
print(task)

type = [1, True, 'hola']
print(type)

print(numbers[0])
print(task[0])

text = 'hola'
# text[0] = 'w'

#no se puede reemplazar el hola de la variable text porque es un str el cual no esta en un conjunto

task[0] = 'whatch platzi'
print(task)

#ahi se cambia el valor 0 de la variable task

print(numbers[:3]) #imprime los numeros desde el inicio de la lista al la posicion 3 (posicion3 excluyente)
print(True in type) # busca si hay True en type respuesta en bool
print('hola' in type) # busca si existe hola en type respuesta en bool