class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        curr_time = 0.0

        for pos, spd in cars:

            t = (target - pos) / spd

            if t > curr_time:
                fleets += 1
                curr_time = t
                
        return fleets

                


        