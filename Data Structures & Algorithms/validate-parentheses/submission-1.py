class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        st = []

        for p in s:
            if p in "}])":

                if not st or st.pop() != p:
                    return False
            else:
                st.append(mp[p])
        return len(st) == 0