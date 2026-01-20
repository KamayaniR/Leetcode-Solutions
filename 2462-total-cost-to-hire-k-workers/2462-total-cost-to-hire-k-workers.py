class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = 0
        right = len(costs) - 1
        left_heap = []
        right_heap = []
        total = 0

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap,costs[left])
                left+=1
            if left <= right:
                heapq.heappush(right_heap,costs[right])
                right-=1
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)

                if left <= right:
                    heapq.heappush(left_heap,costs[left])
                    left+=1
            else:
                total += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1
        return total 





        