class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []

        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed.sort()
        counter = 0

        while pos_speed and pos_speed[0][0] < target:
            for i in range(len(pos_speed) - 1, -1, -1): 
                if i < len(pos_speed) - 1:
                    pos_speed[i][0] = min(pos_speed[i + 1][0], pos_speed[i][0] + pos_speed[i][1])
                else: 
                    pos_speed[i][0] += pos_speed[i][1]
            if pos_speed and pos_speed[-1][0] >= target:

                while pos_speed and pos_speed[-1][0] >= target:
                    pos_speed.pop()   
                counter += 1
              
        return counter

