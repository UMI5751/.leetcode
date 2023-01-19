#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                v1 = nums1[i]
                v2 = nums2[j]
                dictionary[v1 + v2] = dictionary.get(v1 + v2, 0) + 1

        cnt = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                v3 = nums3[i]
                v4 = nums4[j]
                total = v3 + v4
                cnt += dictionary.get(-total, 0)
        return cnt


# @lc code=end

