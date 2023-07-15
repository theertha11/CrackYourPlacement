class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = matrix
        flag = 0 
        positions=[]
        for i in range(0, len(new_matrix)):
            for j in range(0, len(new_matrix[i])):
                if new_matrix[i][j] == 0:
                    positions.append([i,j]) 
                  
        for i in range(0, len(new_matrix)):
            for j in range(0, len(new_matrix[i])):
                if [i,j] in positions:
                    flag = 0
                    if new_matrix[i][j] == 0 and flag==0:
                        for m in range(0, len(new_matrix[i])):
                            matrix[i][m] = 0
                            flag = 1
                        for k in range(0, len(new_matrix)):
                            matrix[k][j] = 0         
                            flag = 1