class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = list(range(n))
        heapq.heapify(rooms)

        inuse = []
        result = [0] * n

        meetings.sort()

        for start, end in meetings:

            # Release all rooms that are available
            while inuse and inuse[0][0] <= start:
                endTime, room = heapq.heappop(inuse)
                heapq.heappush(rooms, room)

            if rooms:
                # Assign the smallest available room
                room = heapq.heappop(rooms)
                heapq.heappush(inuse, (end, room))

            else:
                # Delay the meeting until the earliest room is available
                endTime, room = heapq.heappop(inuse)
                heapq.heappush(inuse, (endTime + end - start, room))

            result[room] += 1

        return result.index(max(result))