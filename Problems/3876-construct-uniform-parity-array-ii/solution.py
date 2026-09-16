class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        oddEvenMap = {'odd':[0, 0], 'even': [0,0]} # store the number and so far lowest number
        resultMap = {'odd':0, 'even':0}
        if len(nums1) <= 1:
            return True
        for num in nums1:
            if num%2 == 0:
                oddEvenMap['even'][0] += 1
                if oddEvenMap['even'][1] == 0 or num < oddEvenMap['even'][1]:
                    oddEvenMap['even'][1] = num
            else:
                oddEvenMap['odd'][0] += 1
                if oddEvenMap['odd'][1] == 0 or num < oddEvenMap['odd'][1]:
                    oddEvenMap['odd'][1] = num
        print(oddEvenMap)
        for num in nums1:
            if num%2 == 0 or (num%2 == 1 and oddEvenMap['odd'][0] > 1 and num > oddEvenMap['odd'][1]):
                resultMap['even'] += 1
            if num%2 == 1 or (num%2 == 0 and oddEvenMap['odd'][0] > 0 and num > oddEvenMap['odd'][1]):
                resultMap['odd'] += 1
        return resultMap['even'] == len(nums1) or resultMap['odd'] == len(nums1)
                
            