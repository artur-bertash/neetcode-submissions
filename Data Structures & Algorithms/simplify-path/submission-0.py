class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []

        for t in path.split('/'):
            if t == '':
                continue
            elif t == "..":
                if st:
                    st.pop()
                continue 
            st.append(t)
        return '/' + '/'.join(st)
        