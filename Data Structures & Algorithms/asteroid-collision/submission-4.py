class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            while st and st[-1] > 0 and ast < 0:
                if st[-1] < -ast:
                    st.pop()
                    continue
                elif abs(ast) == abs(st[-1]):
                    st.pop()
                break
                
            else:
                st.append(ast)
        return st