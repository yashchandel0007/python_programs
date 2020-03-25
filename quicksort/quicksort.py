
def partition(list1, low, high):
    i = low-1
    pivot = list1[high]
    for j in range(low,high+1):
        if list1[j] < pivot:
            i = i+1
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
    temp = list1[i+1]
    list1[i+1] = list1[high]
    list1[high] = temp
    return i+1


def quicksort(list1, low, high):
    if low < high:
        pivot = partition(list1, low, high)
        quicksort(list1, low, pivot-1)
        quicksort(list1, pivot+1, high)

list1 = [12,32,53,13,74,46,232,42,23,53,253,0,4,2,5,2]
quicksort(list1, 0, len(list1)-1)
print(list1)