'''
while True:
  print('se ejecuto')


counter = 0

while counter < 10:
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break # trunca el codigo y llega a contar hasta 15
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    continue #trunca el codigo y cuente desde 15
  print(counter)

'''