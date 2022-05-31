class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, columns = len(grid), len(grid[0])
        fresh, rotten = set(),set()
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    rotten.add((r,c))
        minut = 0
        while fresh:
            minut += 1
            new_rotten = set()
                
            for r,c in rotten:
                for nr, nc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if (r + nr, c + nc) in fresh:
                        new_rotten.add((r + nr, c + nc))
            if not new_rotten:
                return -1
            rotten = new_rotten
            fresh -= new_rotten
        return minut
