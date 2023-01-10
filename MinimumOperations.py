class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[]
        for index,ball in enumerate(boxes):
            steps=0
            for index2,box in enumerate(boxes):
                if box=="1":
                    steps=steps+abs(index2-index)
            res.append(steps)

        return res
