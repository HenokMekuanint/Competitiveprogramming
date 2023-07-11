class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        parents = [[(-1, -1) for _ in range(col)] for _ in range(row)]

        def find(t): # takes tuple, returns tuple
            m, n = t 

            if parents[m][n] == (-1, -1): 
                return -1, -1 # represent water
            if parents[m][n] == (-2, -1): # land that reaches top 
                return (-2, -1)
            if parents[m][n] == (-1, -2): # land that reaches bottom
                return (-1, -2)

            if parents[m][n] != (m, n): # represent land in the middle
                parents[m][n] = find(parents[m][n])
            return parents[m][n]
        
        for i in reversed(range(len(cells))): 
            m, n = cells[i]
            m = m-1
            n = n-1
            if m == 0: 
                parents[m][n] = (-2, -1)
            elif m == row - 1: 
                parents[m][n] = (-1, -2)
            else: 
                parents[m][n] = (m, n)

            for dm, dn in [[0, 1], [0, -1], [1, 0], [-1, 0]]: 
                # check in boundary
                if not (0 <= m+dm < row and 0 <= n+dn < col): 
                    continue 

                pdm, pdn = find((m+dm, n+dn))
                pm, pn = find((m, n))

                # water, skip 
                if (pdm, pdn) == (-1, -1): 
                    continue 
                if (pm, pn) == (-2, -1): 
                    if (pdm, pdn) == (-1, -2): 
                        return i 
                    if pdm >= 0 and pdn >= 0: 
                        parents[pdm][pdn] = (pm, pn)
                elif (pm, pn) == (-1, -2): 
                    if (pdm, pdn) == (-2, -1): 
                        return i 
                    if pdm >= 0 and pdn >= 0: 
                        parents[pdm][pdn] = (pm, pn)
                else: 
                    if pm >= 0 and pn >= 0:   
                        parents[pm][pn] = (pdm, pdn)

        return 0 
