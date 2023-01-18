#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            left, right = self.find_diff_position(left, right, s)
            if left >= right:
                return True
            else:
                return self.is_palindrome(left, right - 1, s) or self.is_palindrome(left + 1, right, s)
    
    def find_diff_position(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return left, right
            else:
                left += 1
                right -= 1
        return left, right
    
    def is_palindrome(self, left, right, s):
        left, right = self.find_diff_position(left, right, s)
        if left >= right:
            return True
        else:
            return False


# @lc code=end

