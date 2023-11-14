class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        operators={"*":lambda x,y: x*y, "/":self.divide, "+": lambda x,y:x+y, "-": lambda x,y: x-y}
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                y=stack.pop()
                x=stack.pop()
                print(x,y,s, operators[s](x,y))
                stack.append(operators[s](x,y))
        return stack.pop()
    def divide(self,x,y):
        if x<0:
            x=-x
            if y<0:
                y=-y
                return x//y
            else:
                return -(x//y)
        elif y<0:
            y=-y
            return -(x//y)
        

s=Solution()

print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
