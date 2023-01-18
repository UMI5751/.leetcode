#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        fisrt_position = -1
        if nums[start] == target:
            fisrt_position = start
        elif nums[end] == target:
            fisrt_position = end

        if fisrt_position == -1:
            return [-1, -1]
        else:
            last_position = fisrt_position
            while last_position < len(nums) - 1 and nums[last_position + 1] == nums[fisrt_position]:
                last_position += 1
            return [fisrt_position, last_position]


# @lc code=end

