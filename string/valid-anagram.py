from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        # Time complexity: O(n log n) - Sorting both strings
        # Space complexity: O(n) - Creating sorted strings
        return sorted(s) == sorted(t)
        """
        """
        # Time complexity: O(n) - Looping through both strings once
        # Space complexity: O(1) - Constant space, using a hashmap
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        for i in t:
            if i not in d:
                return False
            d[i] = d[i]-1
            if d[i]==0:
                del d[i]

        if d=={}:
            return True
        """
        """
        s_count,t_count = {}, {}
        for i in s:
            s_count[i] = s_count.get(i,0) + 1
        for i in t:
            t_count[i] = t_count.get(i,0) + 1
        return s_count==t_count
        """
        if len(s) != len(t):
            return False
        char_count = defaultdict(int)
        for i in s:
            char_count[i] += 1
        for i in t:
            char_count[i] -= 1
        for i in char_count:
            if char_count[i] != 0:
                return False
        return True

