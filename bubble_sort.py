
def bubble_sort(lst :list) -> list:
    for i in range(len(lst)):
        for j in range(len(lst) - i -1):
            if lst[j] > lst[j + 1]:
                lst[j] , lst[j + 1] = lst[j + 1] , lst[j]
    return lst

def bubble_sort_optimized(lst : list) -> list:
    """
    This version of bubble sort implementation is optimized
    because it reduces unnecessary iterations.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                lst[i] , lst[i + 1] = lst[i + 1] , lst[i]
                swapped = True
    return lst
