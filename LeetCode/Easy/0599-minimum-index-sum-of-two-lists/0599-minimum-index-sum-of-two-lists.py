class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        count1 = {word : i for i, word in enumerate(list1)}

        min_num = float('inf')
        res = []

        for index, w in enumerate(list2):
            if w in count1:
                val = count1[w] + index
                
                if val < min_num:
                    min_num = val
                    res = [w]
                
                elif val == min_num:
                    res.append(w)
        
        return res
