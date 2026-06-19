class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True)
        # print(pos_speed)
        fleet_count = 0
        prev_time = -1
        for pos, speed in pos_speed:
            curr_time = (target - pos) / speed
            if curr_time > prev_time:
                prev_time = curr_time
                fleet_count += 1
        
        return fleet_count

        