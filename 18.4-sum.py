#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def find_two_sum(self, sub_target, nums, first, second, result):
        left = second + 1
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == sub_target:
                result.append([nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < sub_target:
                left += 1
            else:
                right -= 1

                


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None or nums == []:
            return []
        if len(nums) < 4:
            return []
        
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                first = i
                second = j
                sub_target = target - (nums[first] + nums[second])
                self.find_two_sum(sub_target, nums, first, second, result)

        return result
                
        
# @lc code=end

