class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        a = 0
        num_str = ""

        while w < len(word) and a < len(abbr):
            if word[w] == abbr[a]:
                w+=1
                a+=1   
                continue
            if not abbr[a].isdigit():
                return False
            while a < len(abbr) and abbr[a].isdigit() :
                if abbr[a] == '0' and not num_str:
                    return False
                num_str+= abbr[a]
                a+=1

            w += 0 if num_str == "" else int(num_str)

            num_str = ""

        return w == len(word) and a == len(abbr)