from collections import OrderedDict
class Twitter:

    def __init__(self):
        self.following = {} # int userId : set(int) setOfFollowingUserId
        self.tweets = OrderedDict() # int tweetId: int userId     

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        counter = 0
        res = []
        for tweet, poster in reversed(self.tweets.items()):
            if poster == userId or (userId in self.following and poster in self.following[userId]):
                res.append(tweet)
                counter += 1
            if counter >= 10:
                break
        return res
            
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
        
