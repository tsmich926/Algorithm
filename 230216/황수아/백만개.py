num= list(map(int, input().split()))
arr = [0] * 1000001 
for i in num:
    arr[i] += 1
for i in range(1000000):
    arr[i+1] += arr[i]
    if arr[i+1] >= 500001:
        print(i+1)
        break


#방법2
def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return Quicksort(left_side) + [pivot] + Quicksort(right_side)

arr = list(map(int,input().split()))
arr=Quicksort(arr)
print(arr[len(arr)//2])