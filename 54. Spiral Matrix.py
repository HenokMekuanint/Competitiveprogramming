class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or matrix == []:
            return matrix
        else:
            #no of rows
            m = len(matrix)
            #no of columns
            n = len(matrix[0])
            #starting row
            k = 0
            #starting column
            l = 0

            #spiral order matrix
            spiral = []

            while k < m and l < n:
                #print the first row from the remaining rows
                for i in range(l, n):
                    spiral.append(matrix[k][i])
                k += 1

                #print the last column from the remaining columns
                for i in range(k, m):
                    spiral.append(matrix[i][n-1])
                n-= 1

                #print the last row from the remaining rows
                if k < m:
                    for i in range(n-1, l-1, -1):
                        spiral.append(matrix[m-1][i])

                    m -= 1

                #print the first column from the remaining columns
                if l < n:
                    for i in range(m-1, k-1, -1):
                        spiral.append(matrix[i][l])

                    l += 1

            return spiral
