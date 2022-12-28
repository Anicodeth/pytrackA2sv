class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        start=n
        if(start%n==0 and start%2==0):
            return n

        while (start%n!=0 or start%2!=0):
            start+=n
        
        return start
