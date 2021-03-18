def merge(list_1, list_2):
    if len(list_1) == 0:
        return list_2
    elif len(list_2) == 0:
        return list_1
    else:
        if list_1[0] <= list_2[0]:
            return [list_1[0]] + merge(list_1[1:], list_2)
        else:
            return [list_2[0]] + merge(list_1, list_2[1:])


def mergesort(list_):
    if len(list_) == 0 or len(list_) == 1:
        return list_
    else:
        middle = len(list_) // 2
        return merge(mergesort(list_[:middle]), mergesort(list_[middle:]))
