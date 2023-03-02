class Solution:
    def getRow(self,rowIndex: int,memo={}) -> List[int]:
        if rowIndex == 0:
                return [1]
        elif rowIndex in memo:
            return memo[rowIndex]
        else:
            prev_row = self.getRow(rowIndex - 1, memo)
            row = [1]
            for i in range(1, rowIndex):
                row.append(prev_row[i-1] + prev_row[i])
            row.append(1)
            memo[rowIndex] = row
            return row
