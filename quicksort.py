def quicksort(list_):
    if len(list_) == 0 or len(list_) == 1:
        return list_
    else:
        low = 1
        high = len(list_) - 1
        pivot = list_[0]
        while True:
            while low < len(list_) and list_[low] < pivot:
                low += 1
            while high > 0 and list_[high] >= pivot:
                high -= 1
            if low < high:
                list_[low], list_[high] = list_[high], list_[low]
            else:
                break
        list_[0], list_[high] = list_[high], list_[0]
    quicksort(list_[:low])
    quicksort(list_[low:])


a = [1, 1, 0, 1, 1]
quicksort(a)
print(a)
