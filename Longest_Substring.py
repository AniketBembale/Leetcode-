# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxi = 0
#         for i in range(len(s)):
#             my_set = set()
#             for j in range(i,len(s)):
#                 if s[j] in my_set:
#                     break
#                 maxi = max(maxi,j-i+1)
#                 my_set.add(s[j])
#         return maxi

## Two Pointer approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        right = 0
        left = 0
        my_dict = {}
        while  right<len(s):
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            
            maxi = max(maxi,right-left+1)
            my_dict[s[right]]=right
            right+=1
        return maxi
            
