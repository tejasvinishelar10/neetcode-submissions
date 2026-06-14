class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        arr = []
        valueList = []
        map = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp in map:
                map[temp].append(s)
            else:
                map[temp]=[s]
        
        return list(map.values())    

