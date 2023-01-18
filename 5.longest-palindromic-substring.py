#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s


        #Enumerate
        #     ans = (0, 0)
        #     for mid in range(len(s)):
        #         ans = max(ans, self.get_palindrom(s, mid, mid))
        #         ans = max(ans, self.get_palindrom(s, mid, mid + 1))

        #     return s[ans[1] : ans[1] + ans[0]]    
        
        # def get_palindrom(self, s, left, right):
        #     while (left >=0 and right < len(s)) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
            
        #     return (right - left - 1, left + 1)

        #Dynamic programming
        s_length = len(s)

        #initial state
        is_palindrome = [[False] * s_length for _ in range(s_length)]
        for i in range(s_length):
            #empty string is palindrome ? 
            is_palindrome[i][i] = True
        for i in range(1, s_length):
            is_palindrome[i][i - 1] = True
        
        #state transferring function
        start, longest = 0, 1
        for length in range(2, s_length + 1):
            for i in range(s_length - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                if is_palindrome[i][j] and length > longest:
                    longest = length
                    start = i

        return s[start : start + longest]

# @lc code=end

