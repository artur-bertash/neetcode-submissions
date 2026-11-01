def isPalin(s, start, end):
    while start <= end: 
        if s[start]== s[end]:
            start+=1
            end -=1
        else:
            return False
    return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        b, e = 0, len(s) - 1


        while b <= e:
            if s[b] == s[e]:
                b+=1
                e-=1
                continue
            else:
                return isPalin(s, b + 1, e) or isPalin(s, b, e - 1)
        return True                            