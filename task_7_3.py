from random import randint

def median_without_sort(arr):
    pivot = arr[0]

    less_med_elems = []
    greater_med_elems = []
    left_med_shoulder = 0
    right_med_shoulder = 0

    for i in array:
        if i < pivot:
            left_med_shoulder += 1
        elif i > pivot:
            right_med_shoulder += 1

        if i in arr:
            if i < pivot:
                less_med_elems.append(i)
            elif i > pivot:
                greater_med_elems.append(i)

    if left_med_shoulder > right_med_shoulder:
        return median_without_sort(less_med_elems)
    elif left_med_shoulder < right_med_shoulder:
        return median_without_sort(greater_med_elems)

    return pivot

n = int(input("Введите положительное целое число: "))
m = 2 * n + 1
print(f"Количество элементов в массиве m = 2 * {n} + 1 = {m}")

max_val = pow(m, 2)
array = []
while len(array) < m:
    x = randint(0, max_val)
    if x not in array:
        array.append(x)

print(f"Медиана для массива {array} из {m} элементов = {median_without_sort(array)}")