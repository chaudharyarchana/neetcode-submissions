class Twitter:

    def __init__(self):
        self.friends = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.friends[userId])
        users.append(userId)
        maxHeap = []
        recentTweets = []
        for user in users:
            maxHeap.extend(self.tweets[user][-10:])
        heapq.heapify(maxHeap)
        while len(recentTweets) < 10 and maxHeap:
             time, tweetId = heapq.heappop(maxHeap)
             recentTweets.append(tweetId)
           
        return recentTweets
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
           return
        self.friends[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
       if followeeId in self.friends[followerId]:
         self.friends[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)