def missing_number(arr, num):

    actual_sum = num * (num + 1) // 2
    current_sum = 0

    for i in arr:
        current_sum = current_sum + i

    missing_num = actual_sum - current_sum

    return missing_num


N = 5
a = [1, 2, 4, 5]
ans = missing_number(a, N)
print("The missing number is:", ans)
