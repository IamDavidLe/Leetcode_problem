class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(num * self.prefix[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        else:
            return int(self.prefix[-1] / self.prefix[len(self.prefix) - k - 1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)