#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        newNums = [(num, index) for index, num in enumerate(nums)]
        newNums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            if newNums[left][0] + newNums[right][0] > target:
                right -= 1
            elif newNums[left][0] + newNums[right][0] < target:
                left += 1
            else:
                return sorted([newNums[left][1], newNums[right][1]])


        return [-1, -1]
# @lc code=end

