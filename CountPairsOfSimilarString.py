class Solution:
    def similarPairs(self, words: List[str]) -> int:
        lis=[]
        for word in words:
            dic={}
            for c in word:
                if c not in dic:
                    dic[c]=1           
            lis.append(sorted(dic))
        pairs=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if lis[i]==lis[j]:
                    pairs+=1
        return pairs
