def find_union(arr1, arr2):
    i = 0
    j = 0
    union_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if arr1[i] not in union_arr:
                union_arr.append(arr1[i])
            i = i + 1
        else:
            if arr2[j] not in union_arr:
                union_arr.append(arr2[j])
            j = j + 1

    while i < len(arr1):
        if arr1[i] not in union_arr:
            union_arr.append(arr1[i])
        i = i + 1

    while j < len(arr2):
        if arr2[j] not in union_arr:
            union_arr.append(arr2[j])
        j = j + 1

    return union_arr


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)
