class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        if len(strs[0]) == 0:
            return ""
        
        base_word = strs[0]

        for i in range(len(base_word)):
            for word in strs[1:]:
                if i == len(word) or base_word[i] != word[i]:
                    return result
            result += base_word[i]

        return result 

        