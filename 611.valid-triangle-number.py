#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def count_triangle(self, nums, longside):
        right = longside - 1
        left = 0
        count = 0

        while left < right:
            if nums[left] + nums[right] > nums[longside]:
                count += right - left
                right -= 1
            else:
                left += 1
        
        return count



    def triangleNumber(self, nums: List[int]) -> int:
        if nums == [] or nums is None:
            return 0
        if len(nums) < 3:
            return 0

        nums.sort()
        result = 0

        for i in range(2, len(nums)):
            longside = i
            result += self.count_triangle(nums, longside)
            i += 1
        return result


# @lc code=end

