def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        balanced=True
        array=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                array.append(i)
            elif i==')' and len(array)!=0 and array[-1]=='(':
                array.pop()
            elif i == '}' and len(array) != 0 and array[-1] == '{':
                array.pop()
            elif i == ']' and len(array) != 0 and array[-1] == '[':
                array.pop()
            elif i==']' and len(array)==0 :
                balanced=False
            elif i=='}' and len(array)==0 :
                balanced=False
            elif i==')' and len(array)==0 :
                balanced=False
            elif i==']' and array[-1]!='[':
                balanced = False
            elif i == '}' and array[-1] != '{':
                balanced = False
            elif i == ')' and array[-1] != '(':
                 balanced = False
        if len(array)!=0:
            balanced=False
        return(balanced)
