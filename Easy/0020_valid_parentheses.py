class Solution:
    def isValid(self,s):

        stack=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                if stack==[] or stack[-1] not in "}])":
                    return False
                stack.pop()
            else:
                stack.append(i)
        return stack==[]
