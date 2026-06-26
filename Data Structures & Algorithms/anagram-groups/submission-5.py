class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            res[temp].append(s)
        
        return list(res.values())