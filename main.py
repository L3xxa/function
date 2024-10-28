from function import dobutok,replacement

a = int(input("Введіть число: "))
b = int(input("Введіть число: "))

a,b = replacement(a, b)
dob = dobutok(a, b)
print(f'Добуток чисел {a} і {b} = {dobutok(a,b)}')