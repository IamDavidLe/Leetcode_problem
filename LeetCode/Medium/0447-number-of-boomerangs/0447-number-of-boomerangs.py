class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return 0

        def distance(point1, point2):
            val = (point1[0] - point2[0])**2  + (point1[1] - point2[1])**2
            return val
        
        res = 0
        for i in range(len(points)):
            seen = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                val = distance(points[i], points[j])
                seen[val] = 1 + seen.get(val, 0)

            
            for count in seen.values():
                res += count * (count - 1)
            
        return res