class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for num in nums:
            count = sum(i for i in nums if i == num)
            if count>n//2:
                return num

        