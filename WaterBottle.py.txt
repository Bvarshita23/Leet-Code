class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        while numBottles>=numExchange:
            exchange=numBottles//numExchange
            total+=exchange
            numBottles=exchange+(numBottles%numExchange)
        return total

        