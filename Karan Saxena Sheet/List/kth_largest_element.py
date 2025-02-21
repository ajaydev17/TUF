from typing import List
import heapq

def get_kth_largest(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    # sort the array in reverse order
    temp = sorted(numbers, reverse=True)

    return temp[k - 1]

def get_kth_largest_heap(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    # gets the k largest elements and return the last one
    kth_largest = heapq.nlargest(k, numbers)[-1]

    # return the kth_largest
    return kth_largest

def get_kth_largest_minheap(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    heapq.heapify(numbers)

    for _ in range(k - 1):
        heapq.heappop(numbers)

    # return the popped element
    return heapq.heappop(numbers)

def get_kth_largest_maxheap(numbers: List[int], k: int) -> int:
    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    max_heap = []

    for num in numbers:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return heapq.heappop(max_heap)
