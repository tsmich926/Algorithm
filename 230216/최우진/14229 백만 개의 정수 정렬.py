def quick_sort(arr):
 
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less, more, equal = [], [], []
    for each in arr:
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort(less) + equal + quick_sort(more)
 
 
arr = list(map(int, input().split()))
 
A = quick_sort(arr)
 
print(A[500000])