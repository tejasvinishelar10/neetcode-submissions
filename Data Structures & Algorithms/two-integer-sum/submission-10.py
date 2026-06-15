class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if target-n in map and map[target-n] != i:
                return [map[target-n], i]
            else:
                map[n]=i

        return []
