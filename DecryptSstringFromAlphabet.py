class Solution:
    def freqAlphabets(self, s: str) -> str:
      start=ord('a')-96
      dic={}
      for n in range(25,8,-1):
          dic[str(start+n)+'#']=chr(start+96+n)
      for n in range(8,-1,-1):
          dic[str(start+n)]=chr(start+96+n)
      for i in dic:
          if i in s:
              s=s.replace(i,dic[i])

      return s
