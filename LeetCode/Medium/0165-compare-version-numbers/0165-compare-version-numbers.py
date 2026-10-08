class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))

        n = max(len(version1), len(version2))
        for i in range(n):
            val1 = version1[i] if i < len(version1) else 0
            val2 = version2[i] if i < len(version2) else 0 

            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
        
        return 0