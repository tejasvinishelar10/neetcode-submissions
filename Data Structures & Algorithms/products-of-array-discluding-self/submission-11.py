class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product,res = 1,[]
        zeroCtr = 0
        for n in nums:
            if n != 0: 
                product = product * n
            else:
                zeroCtr += 1

        if zeroCtr > 1:
            return [0] * len(nums)

        for i, c in enumerate(nums):
            if zeroCtr and c:
                res.append(0)
            elif c:
                res.append(product // c)
            else:
                res.append(product)
            
        return res

