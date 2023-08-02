class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m,n = len(grid), len(grid[0])
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    q = [ (i,j,0,0) ]
                if grid[i][j] in "abcdef":
                    k += 1


        seen = set()

        while q:
            i, j, keys, lev = q.pop(0)

            if grid[i][j] in "abcdef":
                keys |=  1 << (ord(grid[i][j]) - 97)

            if keys == (1 << k)-1:
                return lev

            for a,b in ((0,1),(1,0),(-1,0),(0,-1)):
                x = a+i
                y = b+j
                if 0 <= x < m and 0 <= y < n:
                    if (x,y,keys) not in seen:
                        if grid[x][y] in ".abcdef@":
                            q.append( (x, y, keys, lev + 1) )
                        if grid[x][y] in "ABCDEF":
                            if keys & (1 << (ord(grid[x][y]) - 65)):
                                q.append( (x, y, keys, lev + 1) )
                        seen.add( (x,y,keys) )
        return -1