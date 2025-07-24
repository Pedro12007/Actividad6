def average(sum, length):
    return sum / length

def addition(n):
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

def triangle_area(base, height):
    return (base*height)/2

def is_even_number(num):
    return num % 2 == 0

def grades_average(n):
    sum = 0
    for i in range(n):
        grade = int(input('Ingrese las nota: '))
        sum += grade

    return sum / n