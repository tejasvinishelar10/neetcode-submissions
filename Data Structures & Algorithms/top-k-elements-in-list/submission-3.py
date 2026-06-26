class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        #print(ctr.most_common(k))
        return [x[0] for x in ctr.most_common(k)]