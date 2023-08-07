class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(index: int, count: int, buildings: List[int]) -> int:
            nonlocal max_requests
            if index == len(requests):
                if all(building == 0 for building in buildings):
                    max_requests = max(max_requests, count)
                return
            
            from_building, to_building = requests[index]
            
            # Choose to fulfill the request
            buildings[from_building] -= 1
            buildings[to_building] += 1
            backtrack(index + 1, count + 1, buildings)
            
            # Choose not to fulfill the request
            buildings[from_building] += 1
            buildings[to_building] -= 1
            backtrack(index + 1, count, buildings)
        
        max_requests = 0
        buildings = [0] * n
        backtrack(0, 0, buildings)
        return max_requests