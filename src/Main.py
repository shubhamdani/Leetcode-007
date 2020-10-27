class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            reverseNumber = str(x)
            result = ""
            for c in reversed(reverseNumber):
                if c != "-":
                    result += c
            acresult = int(result)
            if acresult >= 2 ** 31 - 1 or acresult <= -2 ** 31:
                return 0
            else:
                if x < 0:
                    return acresult * -1
                else:
                    return acresult


if __name__ == '__main__':
    print(Solution.reverse(Solution, 123))
