"""Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function that sorts arr.
"""
##bubble sort and insertion sort would each take advantage of the fact that the array is k-messed

def sort_k_messed_array(arr, k):
    for i in range(0, k):
        for idx, val in enumerate(arr):
            if (idx+1)<len(arr):
                if (val > arr[idx+1]):
                    arr[idx], arr[idx+1] = arr[idx+1], arr[idx]

    print(arr)


#driver code
arr=[1,4,5,2,3,7,8,6,10,9]
sort_k_messed_array(arr, 4)
