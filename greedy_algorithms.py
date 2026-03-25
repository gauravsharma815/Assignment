# Fractional Knapsack
def fractional_knapsack(weights, values, capacity):
    ratio = sorted([(v/w, w, v) for w,v in zip(weights,values)], reverse=True)
    total = 0
    for r,w,v in ratio:
        if capacity >= w:
            capacity -= w
            total += v
        else:
            total += r * capacity
            break
    return total

# Activity Selection
def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    result = [activities[0]]
    for i in range(1, len(activities)):
        if activities[i][0] >= result[-1][1]:
            result.append(activities[i])
    return result

# Huffman Coding
import heapq

def huffman(freq):
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
