class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car = []
        for i in range(len(position)):
            car.append((position[i], speed[i]))
        
        car.sort(reverse = True)
        stack = []

        for pos, spd in car:
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
            
        return len(stack)
