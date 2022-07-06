class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        array=[]
        for i in tokens:
            if i == "+" and len(array) > 1:
                x = array.pop()
                y = array.pop()
                array.append(x + y)
            elif i == "-" and len(array) > 1:
                x = array.pop()
                y = array.pop()
                array.append(y - x)
            elif i == "*" and len(array) > 1:
                x = array.pop()
                y = array.pop()
                array.append(x * y)
            elif i == "/" and len(array) > 1:
                x = array.pop()
                y = array.pop()
                if -1<y/x and y/x<1:
                    array.append(0)
                else:
                    array.append(int(y/x))
            else:
                array.append(int(i))

        return array[0]
        
