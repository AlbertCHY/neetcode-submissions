class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        bottleneck = 0
        result = 1

        bottleneck = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            if (target - cars[i][0]) / cars[i][1] > bottleneck:
                result += 1
                bottleneck = (target - cars[i][0]) / cars[i][1]



        return result