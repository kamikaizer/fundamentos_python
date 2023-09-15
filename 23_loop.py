matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matriz[0]) #imprime el primer conjunto
print(matriz[0], matriz[2]) # trae los 2 conjuntos
print(matriz[0][1]) # trae el segundo valor dentro del primer conjunto

for row in matriz:
  print(row) #imprime los conjuntos
  for column in row:
    print(column) #imprime lel conjunto en columnas