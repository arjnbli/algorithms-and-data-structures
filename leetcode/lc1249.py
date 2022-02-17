class Solution:
    #O(n) time| O(n) space
    def minRemoveToMakeValid(self, s: str) -> str:
        #min number of parentheses need to be removed
        #after removal, opening and closing parentheses must be equal
        #remove first unmatched closing parentheses
        stack = []
        for i, char in enumerate(s):
            if char == '(' or char == ')':
                if len(stack) == 0:
                    stack.append((char,i))
                elif char == ')' and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((char, i))

        ignoreIdx = {charIdxPair[1] for charIdxPair in stack}
        finalString = []
        for i, char in enumerate(s):
            if i in ignoreIdx:
                continue
            finalString.append(char)
        return ''.join(finalString)

if __name__ == '__main__':
    solution = Solution()
    print(solution.minRemoveToMakeValid('lee(t(c)o)de)'))