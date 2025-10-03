class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        emptyB=numBottles
        while emptyB>=numExchange: 
            emptyB-=numExchange
            numExchange+=1
            total+=1
            emptyB+=1
        return total