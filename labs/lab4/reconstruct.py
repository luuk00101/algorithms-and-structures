seq = ""
seq_index = 0


def reverse_sort():
    global seq

    upper_bound = int(input())
    seq = input()

    indices = list(range(upper_bound))
    indices = reverse_merge_sort(indices)

    original_permutation = [0] * upper_bound
    for i in range(upper_bound):
        original_permutation[indices[i]] = i + 1

    print(" ".join([str(num) for num in original_permutation]))


def reverse_merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    return merge(reverse_merge_sort(arr[:mid]), reverse_merge_sort(arr[mid:]))


def merge(arr1, arr2):
    global seq
    global seq_index

    result = []
    while (len(arr1) > 0) and (len(arr2) > 0):
        if seq[seq_index] == "<":
            result.append(arr1[0])
            arr1 = arr1[1:]
        else:
            result.append(arr2[0])
            arr2 = arr2[1:]
        seq_index += 1

    result.extend(arr1)
    result.extend(arr2)
    return result


if __name__ == "__main__":
    reverse_sort()
