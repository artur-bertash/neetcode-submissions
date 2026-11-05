class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids: 
            if not st:
                st.append(ast)
                continue
            
            if (ast * st[-1] < 0 and abs(ast) != st[-1]):
                a = st.pop()
                b = ast

                if a > b:
                    a, b = b, a
                
                st.append(b)
            elif st[-1] * ast > 0:
                st.append(ast)
            else:
                st.pop()
        return st

