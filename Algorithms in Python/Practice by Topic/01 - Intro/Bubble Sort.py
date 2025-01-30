arr = [9,3,7,5,5,1,8,3,2,4,4,3,6]

def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(arr))
