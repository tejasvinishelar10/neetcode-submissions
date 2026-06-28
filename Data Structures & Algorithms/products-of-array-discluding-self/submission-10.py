class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, zeroCtr, product = [], 0, 1
        for n in nums:
            if n:
                product = product * n
            else:
                zeroCtr += 1
        
        if zeroCtr > 1:
            return [0] * len(nums)
        
        for i, n in enumerate(nums):
            if n and zeroCtr:
                res.append(0)
            elif n and zeroCtr == 0:
                res.append(product // n)
            else:       #n in zero 
                res.append(product)
        
        return res
