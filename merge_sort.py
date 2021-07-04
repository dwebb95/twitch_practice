def merge_sort(arr):

    """A while loop implementation of merge sort"""

    if len(arr) > 1:  # if the length of the array is > 1 divide it in half
        left_arr = arr[:len(arr) // 2]  # from 0 to the middle
        right_arr = arr[len(arr) // 2:]  # from middle to the end
    if len(arr) == 1:  # if the length of the array is one, it's sorted.
        return arr[0]

    merge_sort(left_arr)  # recursively call and break down the left half
    merge_sort(right_arr)  # recursively call and break down the right half

    i = 0  # left array counter
    j = 0  # right array counter
    k = 0  # sorted array counter


    while i < len(left_arr) and j < len(right_arr): # while both counters are less than their arrays' length
        if left_arr[i] < right_arr[j]:  # if the first index of left array < right
            arr[k] = left_arr[i]  # insert the value of the local left array at position i into the original array at position k
            i += 1  # increment
        else:  # if left is not less than right then always take the right
            arr[k] = right_arr[j]  # insert the value of the local right array at position j into the original array at position k
            j += 1  # increment
        k += 1  # we have inserted a value at position k so increment for the next iteration

    while i < len(left_arr):  # while there are still items in the left array at this step in recursion
        arr[k] = left_arr[i]  # insert the remainder of the sorted local left array to the original array at position k
        k += 1  # increment because that position is filled
        i += 1  # increment because that value has been sorted

    while j < len(right_arr):  # while there are still items in the right array at this step in recursion
        arr[k] = right_arr[j]  # insert the rest of the sorted local right array to the original array at position k
        k += 1  # increment because that position is filled
        j += 1  # increment because that value has been sorted

    return arr  # return the updated array until it makes it back up the call stack to finish modifying array_test


array_test = [2, 5, 6, 3, 5, 8, 9, 0, 2, 1, 4]
merge_sort(array_test)
print(array_test)
