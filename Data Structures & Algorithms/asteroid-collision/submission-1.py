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
            if abs(ast) == abs(st[-1]):
                st.pop()
                continue
            
            while st and st[-1] * ast < 0:
                if abs(st[-1]) < abs(ast):
                    st.pop()
                else:
                    break

        return st

