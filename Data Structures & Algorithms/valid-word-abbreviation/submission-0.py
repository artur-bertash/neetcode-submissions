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
            
            while ord(abbr[a]) >= ord('0') and ord(abbr[a]) <= ord('9'):
                if abbr[a] == '0' and not num_str:
                    return False
                num_str+= abbr[a]
                a+=1

            w += 0 if num_str == "" else int(num_str)
            if w >= len(word):
                return False

        return True