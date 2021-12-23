
a = [10,9,8,7,6,5,4,3,2,1]

def merge_sort(arr, indent=0):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print("{}{} {}".format(' '*indent, left, right))
    if len(left) > 1: left = merge_sort(left, indent+1)
    if len(right) > 1: right = merge_sort(right, indent+1)
    # print("{}{} {}".format(' '*indent, left, right))

    res = []
    while left and right:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

if __name__ == '__main__':
    print(sorted(a))
    print(a)

    res = merge_sort(a, indent=0)
    print(res)