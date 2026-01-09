class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: O(n^2) - The code iterates through the sorted list `nums` once using a for loop, resulting in O(n) time complexity. Within each iteration, it uses two pointers to traverse the remaining part of the list, resulting in O(n) time complexity for each iteration. Therefore, the overall time complexity is O(n^2), where n is the length of the input list `nums`.
        # Space complexity: O(n) - The space complexity of the output list `res` is proportional to the number of valid triplets found, which can be at most O(n) if all elements in `nums` form valid triplets.
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = v+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
        """
        # Time complexity: O(n^2 log n) - Sorting the array takes O(n log n) time. Then, for each pair of elements, performing binary search for the third element takes O(log n) time. Therefore, the overall time complexity is O(n^2 log n).
        # Space complexity: O(n) - The space complexity of the output list `res` is proportional to the number of valid triplets found, which can be at most O(n) if all elements in `nums` form valid triplets.
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = -nums[i] - nums[j]
                # Perform binary search for the third element
                left, right = j + 1, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        res.append([nums[i], nums[j], nums[mid]])
                        break
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return res
        """
                