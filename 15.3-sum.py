#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


    
# @lc code=start
class Solution:
    def two_sum(self, left, right, target, nums, result):
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[right] + nums[left] > target:
                right -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or nums is None:
            return []
        if len(nums) < 3:
            return []

        result = []

        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            self.two_sum(left, right, target, nums, result)

        return result

            


# @lc code=end

