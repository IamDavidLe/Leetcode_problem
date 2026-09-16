class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        
        parent = {x: x for x in nums}
        size = {x : 1 for x in nums}

        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            
            if root_x < root_y:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]

        for num in nums:
            if num + 1 in nums:
                union(num, num + 1)
        
        return max(size.values())