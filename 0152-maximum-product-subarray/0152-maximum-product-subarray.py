class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=mn=res=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],nums[i]*mx,nums[i]*mn)
            mn=min(nums[i],nums[i]*mx,nums[i]*mn)
            mx=temp
            res=max(res,mx)
        return res

        