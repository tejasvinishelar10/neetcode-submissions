class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            if temp in map:
                map[temp].append(s)
            else:
                map[temp]=[s]
        
        return list(map.values())    

