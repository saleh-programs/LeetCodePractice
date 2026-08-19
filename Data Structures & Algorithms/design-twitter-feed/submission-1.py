class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId,userId) 
        heap = []
        for friend in self.follows[userId]:
            for tweet in self.tweets[friend]:
                if len(heap) >= 10:
                    heapq.heappop(heap)
                heapq.heappush(heap, [tweet[0],tweet[1]])
        self.unfollow(userId,userId)  

        return [heapq.heappop(heap)[1] for _ in range(len(heap))][::-1]
  

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
    
