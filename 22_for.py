'''
for element in range(1, 21)
  print(element)
'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'Santi')
for element in my_tuple:
  print(element)

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print(person)
  print('name =>', person['name'])


my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for number in my_list:
  if not number < 0:
    new_list.append(number)

print(new_list)