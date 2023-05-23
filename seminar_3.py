print()
print('Найти загаданное число в массиве')
print()
n = int(input('Введите длину массива n: '))
arr = [0]*n
count = 0
for i in range(n):
    arr[i] = int(input(f'Введите {i+1} элемент массива: '))
print(arr)

x = int(input('Введите искомое число x: '))
for i in range(n):
    if arr[i] == x:
        count += 1
if count > 0:
    print(count)
else:
    print('Такого числа в массиве нет!')
