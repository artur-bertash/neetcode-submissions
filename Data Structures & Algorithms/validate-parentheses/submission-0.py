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
                last = st.pop()
                if last != p:
                    return False
            else:
                st.append(mp[p])
        return True