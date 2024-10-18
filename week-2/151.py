class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        res = []
        i = len(arr)-1
        while i >= 0:
            if (arr[i]) != " ":
                res.append(arr[i])
            i -= 1

        return " ".join(res)

