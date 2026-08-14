class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 1
        high = m*n
        
        #print(m,n)
        while(low <= high):
            #print(low,high)
            mid = int((low + high)/2)

            x = int(mid/n)
            y = int(mid%n)
            # print(low,high,mid)
            # print(x,y)

            if y == 0:
                x = x-1
                y = n

            if matrix[x][y-1] == target:
                return True
            elif matrix[x][y-1] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False



