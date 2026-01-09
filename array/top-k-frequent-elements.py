class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # Time complexity: O(n log n) - Sorting the dictionary by value using sorted() function, where n is the number of unique elements in `nums`.
        # Space complexity: O(n) - Storing the frequency of each unique element in the dictionary `kFreq`, where n is the number of unique elements in `nums`.
        kFreq = {}
        for i in nums:
            kFreq[i] = kFreq.get(i, 0) + 1
        d = dict(sorted(kFreq.items(), key=lambda item: item[1], reverse=True))
        return list(d.keys())[0:k]
        """
        # Time complexity: O(n) - Constructing the frequency dictionary `kFreq` takes O(n) time, where n is the number of elements in `nums`. Constructing the `kList` list of lists also takes O(n) time. The loop to iterate over `kList` and append elements to the result takes O(n) time in the worst case.
        # Space complexity: O(n) - Storing the frequency of each unique element in the dictionary `kFreq` requires O(n) space, where n is the number of elements in `nums`. Storing elements in `kList` requires additional space, but the total space required remains O(n).
        kFreq = {}
        for i in nums:
            kFreq[i] = kFreq.get(i,0) + 1
        kList = [[] for i in range(len(nums)+1)]
        for i,v in kFreq.items():
            kList[v].append(i)
        """
        res=[]
        for i in range(len(kList)-1, 0 , -1):
            for m in kList[i]:
                res.append(m)
            if (len(res)>=k):
                break
        return res[:k]
        """
        return [num for sublist in kList[::-1] for num in sublist][:k]
        