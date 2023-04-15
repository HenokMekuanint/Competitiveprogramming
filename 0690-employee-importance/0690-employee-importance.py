"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        D = {i.id : e for e, i in enumerate(employees)}
        
        def dfs(_id):
            imp=employees[D[_id]].importance
            for subs_id in employees[D[_id]].subordinates:
                imp+=dfs(subs_id)
            return imp
        return dfs(id)
                
            
        
        