class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(log n) - Binary search is used to find the target element. Each iteration of the while loop halves the search space.
        # Space complexity: O(1) - Constant extra space is used regardless of the input size.
        l, r = 0, len(nums) -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
