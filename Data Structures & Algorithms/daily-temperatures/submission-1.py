class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        for i, n in enumerate(temperatures):

            while st and temperatures[st[-1]] < n:
                temperatures[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        while st:
            temperatures[st[-1]] = 0
            st.pop()
        return temperatures