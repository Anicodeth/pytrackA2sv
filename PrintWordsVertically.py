from collections import defaultdict
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(" ")
        word_dict=defaultdict(str)
        max_length=0

        for index,words in enumerate(s):
            if len(words)>max_length:
                max_length=len(words)
                max_index=index
        s1=[]
        for words in s:
            words=words+(" "* (max_length-len(words)))    
            s1.append(words)
        for words in s1:
            for index,char in enumerate(words):
                word_dict[index]=word_dict.get(index,"")+char
        s1=list(word_dict.values())
        s=[]
        for words in s1:
            s.append(words.rstrip())       
        return s
        
