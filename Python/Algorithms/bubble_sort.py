#Сортировка пузырьком - алгоритм, который 

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)- i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(bubble_sort([9, 7, 4, 1, 2]))