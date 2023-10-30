class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        leng = len(nums)
        nums.sort()
        for i in range(1,leng):
            if nums[i] == nums[i-1]:
                return True
        
        return False