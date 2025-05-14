'''🟢 Nivel Básico
1.Saludo personalizado
Crea una función que reciba un nombre y muestre un saludo personalizado.

2.Suma de dos números
Escribe una función que reciba dos números y devuelva su suma.

3.Número par o impar
Crea una función que determine si un número es par o impar.

4.Mayoría de edad
Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

5.Conversor de temperatura
Crea una función que convierta grados Celsius a Fahrenheit.

6.Área de un triángulo
Escribe una función que devuelva el área de un triángulo dado su base y altura.

7.Mayor de una lista
Crea una función que reciba una lista de números y devuelva el mayor.

8.Contar letras
Escribe una función que cuente cuántas veces aparece una letra en una palabra.'''

'''# 1_ Saludo Personalizado
valid = True
def personalized_Greeting(greeting=""):
    print (f"Hello, {greeting}. I hope you have a happy day")
personalized_Greeting(input("Enter his name: "))

# 2_ Suma de dos numeros

sum_number = lambda num1,num2: num1 + num2 
print(sum_number(input("Enter first number: "),input("Enter Second Number: ")))

# 3_ numero par e impar

number_pair = lambda number : f"The number {number} Is pair" if number % 2 == 0 else f"The number {number} is odd"
print(number_pair(int(input("Enter a number: "))))

# 4_ Mayoria de edad

adult = lambda age : f"you are older" if age >= 18 else "You are a minor"
print(adult(int(input("Enter you age: "))))

# 5_conversor de temperatura 

temperature = lambda celsius : celsius* (9/5) + 32
print(temperature(int(input("Enter the degress celsius: "))))

# 6_ Area de un triangulo

area = lambda base , height : (base * height) / 2
print(area(int(input("Enter the base: ")),int(input("Enter the height: "))))

# 7_  Mayor de una lista

def elderly():
    listNumber = [0,2,3,6,9,5,4]
    num = max(listNumber)
    print(f"The number elderly is: {num}")
elderly()

# 8_ contar letras

def count_letters(word):
    for x in word:
        cont = word.count(x)
        print(f"The letters {x} appears {cont} in tha word")
count_letters(input("Enter a word: "))'''

'''🟡 Nivel Intermedio
9.Filtrar pares
Crea una función que reciba una lista de números y devuelva solo los pares.

10.Palíndromo
Escribe una función que determine si un texto es un palíndromo.

11.Factorial
Crea una función que calcule el factorial de un número entero positivo.

12.Eliminar duplicados
Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

13.FizzBuzz
Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

14.Contar vocales
Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

15.Invertir texto
Crea una función que invierta una cadena de texto.

# 9_ filtrar pares
def Pair_and_odd():
    listPairs = [0,1,2,3,4,5,6,7,8,9]
    for x in listPairs:

        if x % 2 == 0:
            print(f"The number {x} is pair ")
        else:
            print(f"The number {x} is odd")
Pair_and_odd()

# 10_ palindromo:
palindromo = lambda word : "Is palindromo" if word == word[::-1] else "Not is palindromo"
print(palindromo(input("Enter a word: ")))

# 11_ Factorial
def factorial(number):
    for i in range(number-1,0,-1):
        number *= i
    print(f"The factorial is {number}")
factorial(int(input("Enter a Number:")))

# 12_Eliminar duplicados

def delete_duplicate():
    listNumber = [4,5,8,4,5,9,7]

    for x in listNumber:
        if listNumber.count(x) > 1:
            listNumber.remove(x)
    print(listNumber)
delete_duplicate()

# 13_ FizzBuzz
def multiple(number):
    if number > 0:
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        if number % 5 == 0:
            print("Buzz")
        if number % 3 == 0:
            print("buzz")
        else:
            print("Not is multiple of 3 and 5")
    else:
        print("Enter a number positive")
multiple(int(input("Enter a number: ")))

# 14_ contar vocales
def vowels(text):
    vowels_defined = "aeiouAEIOU"
    return sum(1 for x in text if x in vowels_defined)

print(vowels(input("Enter a text: ")))

# 15_ invertir texto
invest = lambda text: text[::-1]
print(invest(input("Enter a text:")))'''

'''🔴 Nivel Avanzado
Validar contraseña segura
Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).

Simular dado
Crea una función que simule el lanzamiento de un dado de 6 caras.

Suma de elementos únicos
Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

Generador de contraseñas
Crea una función que genere una contraseña aleatoria de una longitud dada.

Composición de funciones
Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.'''



