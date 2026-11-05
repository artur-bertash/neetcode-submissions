class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids: 
            if not st:
                st.append(ast)
                continue
            
            if ast * st[-1] > 0:
                st.append(ast)
                continue
            if abs(ast) == st[-1]:
                st.pop()
                continue
            if st[-1] < 0 and ast > 0:
                st.append(ast)
                continue

            while st and st[-1] * ast < 0:
                if st[-1] > 0 and st[-1] < abs(ast):
                    st.pop()
                else:
                    break
            if not st or st[-1] < 0 or ast * st[-1] > 0:
                st.append(ast)
        return st

