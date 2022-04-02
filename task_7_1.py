from random import randint

MAX_SIZE = 100

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False
        if flag == True:
            break
    return array

def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array

numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))