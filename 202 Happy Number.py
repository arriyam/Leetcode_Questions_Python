class Solution:
    def isHappy(self, n: int) -> bool:
        def happynum(x):
            x = str(x)
            x = list(map(int, x))
            maxi = 0
            total = 0
            if len(x) == 1:
                if x[0]==1 or x[0]==7:
                    return True
                else:
                    return False
            else:
                for i in range(len(x)):
                    total = (total**2) + (x[i]**2)
                    maxi += total
                    total=0
                return (happynum(maxi))
        return happynum(n)


