import time
import random

# Binary Search
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

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]; i+=1; k+=1
        while j<len(R):
            arr[k]=R[j]; j+=1; k+=1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Max & Min
def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))
    mid = (low + high)//2
    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid+1, high)
    return max(max1, max2), min(min1, min2)
