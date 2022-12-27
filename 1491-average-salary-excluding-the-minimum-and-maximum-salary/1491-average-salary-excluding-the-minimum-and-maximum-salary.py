class Solution:
    def average(self, salary: List[int]) -> float:
        exc_sum=sum(salary)-min(salary)-max(salary)
        return exc_sum/(len(salary)-2)
        