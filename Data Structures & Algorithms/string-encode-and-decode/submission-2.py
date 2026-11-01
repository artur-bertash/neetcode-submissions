class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s 
        return res

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []


        while i < len(s):
            l = ""

            while i < len(s) and s[i] != '#':
                print(s[i])
                l += s[i]
                i+=1
            
            i += 1
            curr = ""
            
            k = 0
            while k < len(s) and k < int(l):
                curr += s[i]
                i += 1
                k += 1
            res.append(curr)
        return res
# funny#3dog#5aple