name = "Martin"
last_name = "Matayoshi"
age = "36"

print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm martin"
print(quote)

quote2 = "Shes said 'Hello' "
print(quote2)

# format

template = "Hola mi nombre es " + name + " y mi apellido es " + last_name + " y tengo " + age + " años"
print('v1', template)

template = "Hola mi nombre es {} y mi apellido es {} y tengo {} años".format(name, last_name, age)
print('v2', template)

template = f"Hola mi nombre es {name} y mi apellido es {last_name} y tengo {age} años"
print('v3', template)
