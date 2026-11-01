def isPalin(s, start, end):
    while start <= end: 
        if not s[start].isalnum():
            start+= 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        
        if s[start].lower() == s[end].lower():
            start+=1
            end -=1
        else:
            return False
    return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        b, e = 0, len(s) - 1


        while b <= e:
            if not s[b].isalnum():
                b+=1
                continue
            if not s[e].isalnum():
                e-=1
                continue
            
            if s[b].lower() == s[e].lower():
                b+=1
                e-=1
                continue

            if not isPalin(s, b + 1, e) and not isPalin(s, b, e - 1):
                return False
            else:
                return True
        return True                            