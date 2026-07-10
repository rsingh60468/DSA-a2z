# INSERTION SORT

arr = [5, 3, 4, 1]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
        print(j)

    
    arr[j+1] = key
    print(arr)

print(arr)

# SELECTION SORT 

arr = [5, 3, 4, 1]
n = len(arr)

for i in range(n):
    minIdx = i
    
    for j in range(i+1, n):
        if arr[j] < arr[minIdx]:
            minIdx = j
    
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)

# BUBBLE SORT

arr = [5, 3, 4, 1]
n = len(arr)

for i in range(n-1):
    swaps = 0
    # isSwap = False
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
            # isSwap = True
    if swaps == 0:
    # if not isSwap:
        break
print(arr)