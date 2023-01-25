def insertionsort(arr):
    for k in range(1, len(arr)):
        key = arr[k]
        j = k
        while j>0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1]= arr[j-1],arr[j]
            j = j-1
            
my_list = [1,9,2,8,3,7,4,6,5]
insertionsort(my_list)
print(my_list)