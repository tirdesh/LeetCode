class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        # Time complexity: O(n) - Iterates through the characters of the string `s` once using two pointers (`l` and `r`), processing each character only once in the while loop.
        # Space complexity: O(min(n, k)) - Uses a set `a` to store unique characters encountered in the current substring. The space complexity is bounded by the size of the character set (usually 256 for ASCII characters) or the length of the string, whichever is smaller.
        a = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            res = max(res, r-l+1)
        return res
        """
        # Time complexity: O(n) - Iterates through the characters of the string `s` once using a for loop, where `n` is the length of the string. Each character is processed only once, and the operations inside the loop (dictionary lookup, updating start pointer, and calculating substring length) are all constant-time operations.
        # Space complexity: O(min(n, k)) - Uses a dictionary `char_index` to store the index of each character encountered in the string. The space complexity is bounded by the size of the character set (usually 256 for ASCII characters) or the length of the string, whichever is smaller.

        longest_length = 0
        start = 0
        char_index = {}

        for i, char in enumerate(s):
            # If the character is already in the dictionary and its index is after the start pointer,
            # update the start pointer to the index after the last occurrence of the repeating character
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the index of the current character
            char_index[char] = i
            
            # Calculate the length of the current substring
            current_length = i - start + 1
            
            # Update the longest substring length
            longest_length = max(longest_length, current_length)

        return longest_length
            
            