class Tree():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def partial(list_, n):
    if n == 0:
        return None
    else:
        if (n - 1) % 2 == 1:
            middle = n // 2 + 1
        else:
            middle = n // 2
        return Tree(
                list_[middle],
                partial(list_[0: middle], middle),
                partial(list_[middle + 1:], (n - middle)),
        )


def tree_to_list(tree):
    if tree_to_list is None:
        return []
    else:
        return (
                tree_to_list(tree.left)
                + [tree.val]
                + tree_to_list(tree.right)
        )


def balance(tree):
    list_ = tree_to_list(tree)
    return partial(list_, len(list_))
