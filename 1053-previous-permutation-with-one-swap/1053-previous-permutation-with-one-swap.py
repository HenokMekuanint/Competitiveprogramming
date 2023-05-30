class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        stack=[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            if stack and arr[stack[-1]]<arr[i]:
                while stack and arr[stack[-1]]<arr[i]:
                    popped_index=stack.pop()
                arr[i],arr[popped_index]=arr[popped_index],arr[i]
                return arr
            else:
                while stack and arr[stack[-1]]==arr[i]:
                    stack.pop()
                stack.append(i)
        return arr
            
                
                
            
                    
        
            
            
            
                
        