class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity: O(n) - The code iterates through the characters of the string once using two pointers `i` and `j`. It performs a constant number of operations for each character comparison. Therefore, the time complexity is linear with respect to the length of the input string `s`.
        # Space complexity: O(1) - The code uses only a constant amount of extra space regardless of the size of the input string. It only uses a few extra variables (`i`, `j`, and temporary variables), which do not scale with the input size.
        i=0
        j=len(s)-1
        
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True
        """
        # Time complexity: O(n) - The code iterates through each character in the string `s` once using a for loop. For each character, it performs a constant number of operations to check if it is alphanumeric and to append it to the string `k`. Additionally, the code compares the string `k` with its reverse using slicing (`k[::-1]`), which also takes linear time. Therefore, the overall time complexity is linear with respect to the length of the input string `s`.
        # Space complexity: O(n) - The code creates a new string `k` to store the alphanumeric characters of `s`, which may have a maximum length equal to the length of `s`. Therefore, the space complexity is linear with respect to the length of the input string.
        k=""
        for char in s:
            if char.isalnum():
                k+=char.lower()
        return k == k[::-1]
        """