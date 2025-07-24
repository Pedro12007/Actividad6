def average(sum, length):
    return sum / length

def addition(n):
    length = n
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

