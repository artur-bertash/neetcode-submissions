class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []


        while i < len(s):
            
            j = i
            while s[j] != '#':
                j += 1

            n = int(s[i:j])

            i = j + 1
            
            
            curr = s[i: i + n]
            res.append(curr)
            i += n
        return res
# funny#3dog#5aple