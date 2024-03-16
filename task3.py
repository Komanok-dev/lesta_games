'''
The fastest algorithm is Counting Sort,
because it uses least quantity of operations
but it consumes memory proportional to maximum digit.
So in case there is unknown maximum digit in array
the best choice is Radix Sort which has time complexity of O(k*n),
where k is the number of digits in the largest number
and n is the number of elements in the array.
'''

def radix_sort(arr):
    # find max length of all digits in array
    max_len = max([len(str(digit)) for digit in arr])
    # create temporary buckets for sorting digits 0-9
    temp_arr = [[] for _ in range(10)]

    for i in range(max_len):
        for digit in arr:
            # get digits one by one each iteration from last to first
            x = (digit // 10 ** i) % 10
            # put digit into the x bucket in temp array
            temp_arr[x].append(digit)
        # recreate initial array considering sorting in buckets
        arr = [k for j in temp_arr for k in j]
        # clear buckets
        temp_arr = [[] for _ in range(10)]

    return arr
