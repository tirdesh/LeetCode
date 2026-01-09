from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        """
        # Time complexity: O(n) - Iterates through each character of the string `s` once, where `n` is the length of the string. Operations inside the loop, such as appending to the list, checking conditions, and accessing elements, all take constant time.
        # Space complexity: O(n) - Uses a list `a` to simulate a stack, which may contain up to `n` elements in the worst case, where `n` is the length of the input string `s`.
        a = []
        validMap = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in s:
            if i in ['(', '{', '[']:
                a.append(i)
            elif a and validMap.get(a[-1], False) == i:
                continue
            else:
                return False
        return len(a) == 0
        """


        # Time complexity: O(n) - Iterates through each character of the string `s` once, where `n` is the length of the string. Operations inside the loop, such as appending to the deque, popping elements, and checking conditions, all take constant time.
        # Space complexity: O(n) - Uses a deque `stack` to simulate a stack, which may contain up to `n` elements in the worst case, where `n` is the length of the input string `s`.

        stack = deque()
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack