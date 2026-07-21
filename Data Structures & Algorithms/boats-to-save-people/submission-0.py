class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        result = 0

        while left <= right:
            if left == right:
                left += 1
            if people[right] + people[left] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            result += 1

        return result