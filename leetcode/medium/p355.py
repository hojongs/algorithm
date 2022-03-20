"""
https://leetcode.com/problems/design-twitter/
"""
from typing import List, Tuple

TweetId = int
Sequence = int
UserId = int


class Twitter:
    def __init__(self):
        self.tweetDict: dict[UserId, List[Tuple(TweetId, Sequence)]] = dict()
        # Followees of a user should be unique: Use set rather than List
        self.followeeSet: dict[UserId, set[UserId]] = dict()
        self.sequence: Sequence = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweetDict.setdefault(userId, [])
        tweets.append((tweetId, self.sequence))
        self.sequence += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all tweets of the user
        newsFeed = self.tweetDict.setdefault(userId, [])[:]
        # Get all tweets of followees
        followees = self.followeeSet.setdefault(userId, set())
        for f in followees:
            tweets = self.tweetDict.setdefault(f, [])
            for t in tweets:
                newsFeed.append(t)
        # Sort by sequence
        newsFeed.sort(key=lambda x: x[1], reverse=True)
        # Return most 10 recent tweets without sequence
        return list(map(lambda x: x[0], newsFeed))[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.followeeSet.setdefault(followerId, set())
        followees.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followeeSet.setdefault(followerId, set())
        try:
            followees.remove(followeeId)
        except KeyError:
            pass

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
