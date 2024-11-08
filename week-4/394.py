class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0
        for i in s:
            if i == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif i == "]":
                stack_num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + stack_num * string
            elif i.isdigit():
                num = num*10 + int(i)
            else:
                string += i

        return string   