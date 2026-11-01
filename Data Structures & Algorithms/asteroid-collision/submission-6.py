class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            while st and st[-1] > 0 and ast < 0:
                # 3 cases
                # keep going ast
                # equal break
                # ast breaks
                if -ast > st[-1]:
                    st.pop()
                    continue
                elif -ast == st[-1]:
                    st.pop()
                    break
                else:
                    break
            else:
                st.append(ast)
        return st