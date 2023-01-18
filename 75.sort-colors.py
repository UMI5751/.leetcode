#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def partition(self, nums, k):
        wall_pointer = -1
        for i in range(len(nums)):
            if nums[i] < k:
                wall_pointer += 1
                nums[wall_pointer], nums[i] = nums[i], nums[wall_pointer]


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition(nums, 1)
        self.partition(nums, 2)


# @lc code=end

