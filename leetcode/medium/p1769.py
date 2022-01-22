"""
1769. Minimum Number of Operations to Move All Balls to Each Box
"""
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        onecnt = [0] * len(boxes)
        answer = [0] * len(boxes)
        # traverse reversely and store cnt of one right-side
        if boxes[-1] == '1':
            onecnt[-1] = 1
        else:
            onecnt[-1] = 0
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i] == '1':
                onecnt[i] = onecnt[i+1] + 1
            else:
                onecnt[i] = onecnt[i+1]
        # first elem of the one cnt is the number of all ones.
        allonecnt = onecnt[0]
        # calculate min number of ops on first box
        for k in range(1, len(boxes)):
            if boxes[k] == '1':
                answer[0] += k
        # calculate the number on the next box by using the number of the first box, the one cnt
        for i in range(1, len(answer)):
            # right-side ones are close
            answer[i] = answer[i-1] - onecnt[i]
            # left-side ones are away
            answer[i] += allonecnt - onecnt[i]
        return answer
