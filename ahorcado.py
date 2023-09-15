import random

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'juego', 'ahorcado', 'computadora', 'diversion']

# Función para elegir una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Función principal del juego
def juego_ahorcado():
    palabra_secreta = seleccionar_palabra()
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []

    print("¡Bienvenido al juego del ahorcado!")

    while True:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            palabra_actual = mostrar_palabra(palabra_secreta, letras_adivinadas)
            print("Palabra actual: " + palabra_actual)

            if palabra_actual == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra: " + palabra_secreta)
                break
        else:
            intentos += 1
            print("Letra incorrecta. Intentos restantes:", intentos_maximos - intentos)

            if intentos >= intentos_maximos:
                print("¡Perdiste! La palabra era:", palabra_secreta)
                break

if __name__ == "__main__":
    juego_ahorcado()