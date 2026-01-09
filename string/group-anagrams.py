class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_dict = defaultdict(list)
        for i in strs:
            c_list = [0] * 26
            for j in i:
                c_list[ord(j) - ord('a')] +=1
            c_dict[tuple(c_list)].append(i)
        return list(c_dict.values())