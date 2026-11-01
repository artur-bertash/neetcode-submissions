class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for word in strs:
            cv = [0] * 26
            for ch in word:
                cv[ord(ch) - ord('a')]+=1
            
            hk = ""
            for d in cv:
                hk += str(d)
                hk += "+"
            mp.setdefault(hk, []).append(word)
        
        res = []
        for key, val in mp.items():
            res.append(val)
        return res
