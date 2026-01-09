class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        # Time complexity: O(n) - The function iterates through the input list `nums` three times, each time with a complexity of O(n). Therefore, the overall time complexity is O(3n), which is equivalent to O(n), where n is the length of the input list.
        # Space complexity: O(n) - The function uses three additional lists: `prefix`, `postfix`, and `res`, each of which may contain up to n elements, where n is the length of the input list `nums`. Therefore, the space complexity is O(3n), which simplifies to O(n).
        res=[]
        prefix, postfix = [], []
        premul, postmul = 1,1
        for i in nums:
            premul *= i
            prefix.append(premul)        
        for i in nums[::-1]:
            postmul *= i
            postfix.insert(0,postmul)
        for i in range(len(nums)):
            prefix_val = prefix[i-1] if i-1 >= 0 else 1  # Check if i-1 is within range
            postfix_val = postfix[i+1] if i+1 < len(nums) else 1  # Check if i+1 is within range
            res.append(prefix_val * postfix_val)  # Multiply prefix_val and postfix_val
        return res
        """

        res = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res