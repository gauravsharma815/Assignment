import time
import random

# -------------------------------
# 1. Binary Search (Recursive)
# -------------------------------
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    return -1


# -------------------------------
# 2. Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# -------------------------------
# 3. Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# -------------------------------
# 4. Max and Min (Divide & Conquer)
# -------------------------------
def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))

    mid = (low + high) // 2
    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)


# -------------------------------
# 5. Strassen’s Matrix Multiplication
# -------------------------------
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix


# -------------------------------
# TESTING & TIMING
# -------------------------------
if __name__ == "__main__":

    arr = random.sample(range(1000), 100)

    # Binary Search
    sorted_arr = sorted(arr)
    x = sorted_arr[50]
    start = time.time()
    index = binary_search(sorted_arr, 0, len(sorted_arr)-1, x)
    print("Binary Search Index:", index)
    print("Time:", time.time() - start)

    # Merge Sort
    temp = arr.copy()
    start = time.time()
    merge_sort(temp)
    print("\nMerge Sort Time:", time.time() - start)

    # Quick Sort
    temp = arr.copy()
    start = time.time()
    quick_sorted = quick_sort(temp)
    print("Quick Sort Time:", time.time() - start)

    # Max Min
    start = time.time()
    mx, mn = max_min(arr, 0, len(arr)-1)
    print("\nMax:", mx, "Min:", mn)
    print("Time:", time.time() - start)

    # Strassen Matrix
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    start = time.time()
    result = strassen(A, B)
    print("\nStrassen Result:")
    for row in result:
        print(row)
    print("Time:", time.time() - start)
