class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = Counter(nums)
        
        # Create max heap
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)
        
        # Extract top k elements
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
