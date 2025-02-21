from typing import List
import heapq

def get_kth_smallest(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    # sort the array in reverse order
    temp = sorted(numbers)

    return temp[k - 1]

def get_kth_largest_heap(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    # gets the k largest elements and return the last one
    kth_largest = heapq.nsmallest(k, numbers)[-1]

    # return the kth_largest
    return kth_largest

def get_kth_largest_minheap(numbers: List[int], k: int) -> int:

    # check the base condition
    if len(numbers) < 1:
        return "List is empty"

    # take the first k element
    min_heap = numbers[:k]

    # convert it into a min heap
    heapq.heapify(min_heap)

    # iterate through the remaining elements
    for num in numbers[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    # return the root of the heap
    return min_heap[0]