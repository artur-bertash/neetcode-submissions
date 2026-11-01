class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s2 , s1 = s1, s2
        counter1 = [0] * 26
        for ch in s2:
            counter1[ord(ch) - ord('a')] += 1
        counter2 = [0] * 26
        l = 0

        for r in range(len(s1)):
            
            counter2[ord(s1[r]) - ord('a')] += 1
            if r - l + 1 > len(s2):
                counter2[ord(s1[l]) - ord('a')] -= 1
                l += 1
            if counter2 == counter1:
                return True
            
        return False