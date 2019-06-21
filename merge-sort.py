def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge(a, b):
    res = []
    a_idx, b_idx = 0, 0

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a): res.extend(b[b_idx:])
    else:               res.extend(a[a_idx:])

    return res

def merge_sort(a):
    if len(a) <= 1: return a
    mid = int(len(a)/2)
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(left, right)

a = create_array()
print(a)
s = merge_sort(a)
print(s)
