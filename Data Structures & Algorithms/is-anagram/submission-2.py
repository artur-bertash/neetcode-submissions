class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable1 = {}
        hashtable2 = {}
        for el_s in s:
            if  el_s not in hashtable1:
                hashtable1[el_s] = 0
            hashtable1[el_s] += 1
        for el_t in t:
            if  el_t not in hashtable2:
                hashtable2[el_t] = 0
            hashtable2[el_t] += 1
        return hashtable1 == hashtable2