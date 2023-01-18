#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:      
            if not self.is_valid(s[left]):
                left += 1
            elif not self.is_valid(s[right]):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True

            

    
    def is_valid(self, character):
        if character.isdigit() or character.isalpha():
            return True
        
# @lc code=end

