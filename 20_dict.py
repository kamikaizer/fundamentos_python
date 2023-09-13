person = {
  'name': 'nico',
  'last_name': 'molina',
  'lang': ['python', 'Js'],
  'age': 37
}

print(person)

person['name'] = 'martin'
person['age'] -= 10
person['lang'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('items')
print(person.items()) #trae en tuplas el titulo y el valor

print('keys')
print(person.keys()) # trae solo los titulos

print('values')
print(person.values()) #trae solo los valores

person['twitter'] = '@nicobites'
person['name'] = 'Felipe'
del person['age']
print(list(person.keys()))
print(list(person.values()))