class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        num, total = list(map(int, str(num))), 0
        while len(num) != 1:
            for i in range(len(num)):
                a = total + num[i]
                total = a
            num = str(total)
            num, total = list(map(int, str(num))), 0
        return (num[0])

