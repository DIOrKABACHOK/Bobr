from random import *

N = int(input("Задайте размерность массива: "))


def generate_array(N):
    array = []
    for i in range(1, N + 1):
        array.append(i)

    return array


array = generate_array(N)
print('Массив:')
print(array)

def find(array):
    num_dict = {}
    K = randint(1, 15)
    print(f'\nK = {K}')
    for i in range(len(array)):
        complement = K - array[i]
        if complement in num_dict:
            return [num_dict[complement], i + 1]
        num_dict[array[i]] = i + 1
    return -1


ans = find(array)
count = 0
while ans == -1:
    ans = find(array)
    count += 1

print(f'Ответ: {ans}')
print(f'Количестов неудачных попыток: {count}')