class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vec_counter = [0] * 26

        for ch in s:
            vec_counter[ord(ch) - ord('a')]+= 1
        
        for ch in t:
            vec_counter[ord(ch) - ord('a')]-= 1
        
        for count in vec_counter:
            if count != 0:
                return False
        return True