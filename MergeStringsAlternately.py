class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2)
        if w1 > w2:
            dif=w1-w2
            word2=word2+(" "*dif)
        elif w2 > w1:
            dif=w2-w1
            word1=word1+(" "*dif)

        newstring=""
        for i in range(len(word1)):
            newstring=newstring+word1[i]+word2[i]

        return newstring.replace(" ",'')
