class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        # Time complexity: O(n log n) - Sorting the list of integers takes O(n log n) time, where n is the number of elements in the list. The loop then iterates through the sorted list once, taking O(n) time.
        # Space complexity: O(1) - The algorithm uses only a constant amount of extra space regardless of the input size. Sorting is performed in-place, and only a few variables are used to keep track of the current and maximum lengths.
        
        if not nums:
            return 0
        
        nums.sort()
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)
        """
        nSet = set(nums)
        maxL = 0
        for n in nSet:
            if n-1 not in nSet:
                l = 0
                while n+l in nSet:
                    l+=1
                maxL = max(l, maxL)
        return maxL