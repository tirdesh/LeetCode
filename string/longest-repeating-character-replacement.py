class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time complexity: O(n) - Iterates through the characters of the string `s` once using a for loop, where `n` is the length of the string. Each character is processed only once, and the operations inside the loop (updating the countMap, adjusting the left pointer, and updating the result) are all constant-time operations.
        # Space complexity: O(1) - Uses a fixed-size array `countMap` of size 26 to store the count of each character encountered in the string. The space complexity is independent of the size of the input string `s`.
        countMap = [0] * 26
        l = 0
        res = 0
        for r in range(len(s)):
            countMap[ord(s[r]) - ord('A')] +=1
            if (r-l+1) - max(countMap) > k :
                countMap[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
        
