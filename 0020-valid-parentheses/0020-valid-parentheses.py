class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(','}':'{',']':'['}
        stack = []

        for brac in s:
            if brac in brackets.values():
                stack.append(brac)
            elif brac in brackets.keys():
                if stack and stack[-1]==brackets[brac]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if not stack else False


        