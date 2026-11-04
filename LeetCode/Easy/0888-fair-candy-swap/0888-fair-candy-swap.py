class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        diff = (sum(bobSizes) - sum(aliceSizes)) // 2
        bobSizes = set(bobSizes)
        for a in aliceSizes:
            if diff + a in bobSizes:
                return [a, a + diff]