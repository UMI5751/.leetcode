#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    #quick sort
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     if nums is None:
    #         return
        
    #     self.quick_sort(0, len(nums) - 1, nums)
    #     return nums

    
    # def quick_sort(self, start, end, nums):
    #     if start >= end:
    #         return

    #     pivot = nums[(start + end) // 2]
    #     left = start
    #     right = end

    #     while left <= right:
    #         while (left <= right) and (nums[left] < pivot):
    #             left += 1
    #         while (left <= right) and (nums[right] > pivot):
    #             right -= 1
            
    #         if left <= right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     self.quick_sort(start, right, nums)
    #     self.quick_sort(left, end, nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        if nums is None:
            return
        
        temp = [0] * len(nums)
        self.merge_sort(nums, temp, 0, len(nums) - 1)
        return nums
    
    def merge_sort(self, nums, temp, start, end):
        if start >= end:
            return

        self.merge_sort(nums, temp, start, (start + end) // 2)
        self.merge_sort(nums, temp, (start + end) // 2 + 1, end)
        self.merge(nums, temp, start, end)

    def merge(self, nums, temp, start, end):
        middle = (start + end) // 2
        leftInd = start
        rightInd = middle + 1
        ind = start

        while (leftInd <= middle) and (rightInd <= end):
            if nums[leftInd] < nums[rightInd]:
                temp[ind] = nums[leftInd]
                leftInd += 1
                ind += 1
            else:
                temp[ind] = nums[rightInd]
                rightInd += 1
                ind += 1
            
        while leftInd <= middle:
            temp[ind] = nums[leftInd]
            leftInd += 1
            ind += 1

        while rightInd <= end:
            temp[ind] = nums[rightInd]
            rightInd += 1
            ind += 1
        
        i = start
        while i <= end:
            nums[i] = temp[i]
            i += 1

# @lc code=end

