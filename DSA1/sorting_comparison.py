import time
import random
import matplotlib.pyplot as plt

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
                arr[k]=L[i]; i+=1
            else:
                arr[k]=R[j]; j+=1
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
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Cases
def best(n): return list(range(n))
def worst(n): return list(range(n,0,-1))
def avg(n): return random.sample(range(n*10), n)

def measure(f, arr):
    start = time.time()
    f(arr)
    return time.time() - start

def main():
    sizes = [100, 500, 1000, 2000]

    m_b, m_a, m_w = [], [], []
    q_b, q_a, q_w = [], [], []

    for s in sizes:
        m_b.append(measure(merge_sort, best(s)))
        q_b.append(measure(quick_sort, best(s)))

        m_a.append(measure(merge_sort, avg(s)))
        q_a.append(measure(quick_sort, avg(s)))

        m_w.append(measure(merge_sort, worst(s)))
        q_w.append(measure(quick_sort, worst(s)))

    plt.plot(sizes, m_b, label="Merge Best")
    plt.plot(sizes, m_a, label="Merge Avg")
    plt.plot(sizes, m_w, label="Merge Worst")

    plt.plot(sizes, q_b, label="Quick Best")
    plt.plot(sizes, q_a, label="Quick Avg")
    plt.plot(sizes, q_w, label="Quick Worst")

    plt.xlabel("Input Size")
    plt.ylabel("Time")
    plt.title("Sorting Comparison")
    plt.legend()

    plt.savefig("plots/sorting_comparison.png")
    plt.show()

if __name__ == "__main__":
    main()
