class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        indx = []
        for i, n in enumerate(temperatures):

            while st and st[-1] < n:
                temperatures[indx[-1]] = i - indx[-1]
                st.pop()
                indx.pop()
            st.append(n)
            indx.append(i)
        for n in st:
            temperatures[indx[-1]] = 0
            indx.pop()
        return temperatures