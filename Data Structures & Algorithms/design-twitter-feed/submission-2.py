class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.posts = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        targets = [userId]
        for user in self.users[userId]:
            targets.append(user)
        for i in range(len(targets)):
            postlist = self.posts[targets[i]]
            for post in postlist:
                heapq.heappush(heap, post)
                if len(heap) > 10:
                    heapq.heappop(heap)
        result = []
        heapq.heapify_max(heap)
        for i in range(len(heap)):
            result.append(heapq.heappop_max(heap)[1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.users[followerId]:
            self.users[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
