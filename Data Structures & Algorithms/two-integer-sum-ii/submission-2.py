class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(numbers):
            if target-n in map and i != map[target-n]:
                return [map[target-n]+1, i+1]
            else:
                map[n] = i
        
        return []
