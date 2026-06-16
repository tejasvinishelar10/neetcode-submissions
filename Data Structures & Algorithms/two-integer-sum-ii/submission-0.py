class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        while L < R:
            if numbers[L] + numbers [R] == target:
                print(L, R)
                return [L+1, R+1]
            elif numbers[L] + numbers [R] > target:
                print(L, R)
                R -= 1
            else: 
                print(L, R)
                L += 1
        
        return []

