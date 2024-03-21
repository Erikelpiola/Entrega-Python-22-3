import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Ahora existe un número máximo de fallos permitidos
max_fails = 4
fails=0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("""Seleccionar una dificultad para empezar: 
      0.Fácil
      1.Media
      2.Difícil""")
option= int(input())
match option:
    #Dificultad que muestra las vocales de la palabra
    case 0:
        letters = []
        guessed_letters=["a","e","i","o","u"]
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed="".join(letters)
    #Dificultad que muestra la letra inicial y final de la palabra
    case 1:
        letters= []
        for letter in secret_word:
            if letter==secret_word[0] or letter==secret_word[-1]:
                guessed_letters.append(letter)
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed="".join(letters)
    case 2:
        word_displayed = "_" * len(secret_word)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
#Inserto un limite de fallos
while fails<max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    #Si llega a pasar que se pulse "Enter", se pedirán letras válidas y no consumirá el intento del jugador
    #Además tomo la precondición de que el jugador no va a ingresar caracteres especiales,numeros o una cadena de caracteres.
    while letter=="":
        letter = input("Error, ingresar una letra válida: ").lower()
     # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra")
        fails=fails+1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_fails} intentos.")
    print(f"La palabra secreta era: {secret_word}")