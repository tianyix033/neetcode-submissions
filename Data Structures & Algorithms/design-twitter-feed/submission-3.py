import heapq
class Twitter:

    def __init__(self):
        self.following = {} # int userId : set(int) setOfFollowingUserId
        self.tweets = {}    # int userId : heap(int timestamp, int tweetId)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        heapq.heappush(self.tweets[userId], (self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        lst = []
        if userId in self.following:
            for followee in self.following[userId]:
                lst.extend(heapq.nsmallest(10, self.tweets[followee]))
        if userId in self.tweets and (userId not in self.following or userId not in self.following[userId]):
            lst.extend(heapq.nsmallest(10, self.tweets[userId]))
        heapq.heapify(lst)
        tweets = heapq.nsmallest(10, lst)
        return [tweet[1] for tweet in tweets]
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # we do not raise error if followee is not already followed by follower
        # design choice; could be changed 
        if followerId not in self.following:
            return
        self.following[followerId].discard(followeeId)
        
