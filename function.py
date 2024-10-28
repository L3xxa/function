

def replacement(a,b):
    if a > b:
        a, b = b, a
    return a, b

def dobutok(a, b):
    result = 1
    for i in range(a, b + 1):  # Включаємо b в діапазон
        result *= i
    return result

