def partition(lst : list ,start , end) -> int:
    pivot = lst[end]
    i = start - 1
    for j in range(len(lst)):
        if lst[j] <= pivot:
            i += 1
            lst[i] , lst[j] = lst[j] , lst[i]
    i += 1
    lst[i] , lst[end] = lst[end] , lst[i]
    return i   

def quick_sort(lst , start , end) -> list:
    if start <= end:
        pi = partition(lst, start , end)
        quick_sort(lst, start , pi - 1)
        quick_sort(lst , pi + 1 , end)
    return lst
