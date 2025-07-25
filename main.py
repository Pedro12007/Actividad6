def average(sum=1, length=1):
    return sum / length

def addition(n=1):
    sum = 0
    positive = 0
    negative = 0
    for i in range(n):
        number = float(input(f'Ingrese el número ({i+1}): '))
        sum += number
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1

    return sum, positive, negative

def triangle_area(base=1, height=1):
    return (base*height)/2

def is_even_number(num=2):
    if num % 2 == 0:
        return 'Es par'
    else:
        return 'Es impar'

def grades_average(n=1):
    sum = 0
    for i in range(n):
        grade = int(input('Ingrese las nota: '))
        sum += grade

    return sum / n

def max_and_min_num(n=1):
    numbers = []
    for i in range(n):
        num = int(input('Ingrese el número: '))
        numbers.append(num)

    return max(numbers), min(numbers)

while True:
    print('Opciones:')
    print('1. Sumar, obtener promedio, positivos y negativos')
    print('2. Calcular el área de un triángulo')
    print('3. Verificar si un número es par o impar')
    print('4. Calcular el promedio de n calificaciones')
    print('5. Ingresar n números y mostrar el mayor y el menor')
    print('6. Salir del programa')

    option = input('Ingrese una opción: ')
    match option:
        case '1':
            n = int(input('Ingrese la cantidad de números que desea sumar: '))
            result = addition(n)
            print()
            print(f'La suma de los números es: {result[0]}')
            print(f'El promedio de los números sumados es: {average(result[0], n)}')
            print(f'La cantidad de positivos es: {result[1]}')
            print(f'La cantidad de negativos es: {result[2]}')
            print()

        case '2':
            base = float(input('Ingrese la base del triangulo (cm): '))
            height = float(input('Ingrese la altura del triangulo (cm): '))
            print(f'El area del triangulo es de: {triangle_area(base, height)}cm')
            print()

        case '3':
            number = int(input('Ingrese el número: '))
            print(is_even_number(number))
            print()

        case '4':
            n = int(input('Ingrese la cantidad de notas: '))
            print(f'El promedio de las notas es: {grades_average(n)}')
            print()

        case '5':
            n = int(input('Ingrese la cantidad de números a evaluar: '))
            max_and_min = max_and_min_num(n)
            print(f'El número mayor es: {max_and_min[0]}')
            print(f'El número menor es: {max_and_min[1]}')
            print()

        case '6':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.')
            print()