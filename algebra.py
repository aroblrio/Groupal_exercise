class LinearAlgebra:

    def input_matrix(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        matrix = []
        print("Enter the elements of the matrix:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
                row.append(element)
            matrix.append(row)
        return matrix

    def matrix_sum(self, matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result

    def matrix_multiply(self, matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                val = 0
                for k in range(len(matrix2)):
                    val += matrix1[i][k] * matrix2[k][j]
                row.append(val)
            result.append(row)
        return result

    def determinant(self, matrix):
        if len(matrix) != len(matrix[0]):
            raise ValueError("Determinant can only be calculated for a square matrix")
        
        if len(matrix) == 1:
            return matrix[0][0]
        
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for i in range(len(matrix)):
            sign = (-1) ** i
            minor = self.get_minor(matrix, 0, i)
            det += sign * matrix[0][i] * self.determinant(minor)
        return det

    def matrix_range(self, matrix):
        min_val = min(min(row) for row in matrix)
        max_val = max(max(row) for row in matrix)
        return max_val - min_val

    def get_minor(self, matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]