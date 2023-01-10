class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        index1=num1.index("+")
        index2=num2.index("+")
        x1, y1 = int(num1[:index1]), int(num1[index1+1:-1])
        x2, y2 = int(num2[:index2]), int(num2[index2+1:-1])
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"
