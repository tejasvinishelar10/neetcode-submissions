class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(Counter(nums))
        freq = Counter(nums)
        print([x[0] for x in freq.most_common(k)])
        ans = []
        return [x[0] for x in freq.most_common(k)]
        