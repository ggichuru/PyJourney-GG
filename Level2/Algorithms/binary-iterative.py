def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        #check if x is present at mid
        if arr[mid] < x:
            low = mid + 1
        #if x is greater, ignore the left half
        elif arr[mid] > x:
            high = mid - 1
        #if x is smaller, ignore the right half
        else:
            return mid
    #if we reach here, then element was not present
    return -1

arr = [2,3,4,10,40]
x = 10

result = binary_search(arr, x)

if result != -1:
    print('Element is present at index ', str(result))
else:
    print('Element is not present in array')