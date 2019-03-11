import random
import copy

class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = []

        for row in range(rows):
            self.data.append([])
            for column in range(columns):
                self.data[row].append(0)

    @staticmethod
    def from_array(array):

        result = Matrix(len(array), 1)

        for row in range(len(array)):
            result.data[row][0] = array[row]

        return result

    @staticmethod
    def to_array(matrix):
        array = []

        for row in range(matrix.rows):
            for column in range(matrix.columns):
                array.append(matrix.data[row][column])

        return array

    @staticmethod
    def transpose_matrix(matrix):
        
        result = Matrix(matrix.columns, matrix.rows)

        for row in range(matrix.rows):
            for column in range(matrix.columns):
                result.data[column][row] = matrix.data[row][column]

        return result

    def randomize(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.data[row][column] = random.uniform(-1, 1) * 2 - 1
    
    @staticmethod
    def multiply_matrix(a, b):
        
        result = Matrix(a.rows, b.columns)

        for row in range(result.rows):
            for column in range(result.columns):

                addition = 0
                for s in range(a.columns):
                    addition += a.data[row][s] * b.data[s][column]

                result.data[row][column] = addition
                    
        return result
        
    def multiply(self, n):
        
        for row in range(self.rows):
            for column in range(self.columns):
                self.data[row][column] *= n

    def map(self, func):
        for row in range(self.rows):
            for column in range(self.columns):
                val = self.data[row][column]
                self.data[row][column] = func(val)

    @staticmethod
    def map_matrix(matrix, func):
        for row in range(matrix.rows):
            for column in range(matrix.columns):
                val = matrix.data[row][column]
                matrix.data[row][column] = func(val)

        return matrix

    def add(self, n):

        if type(n) is Matrix:
            for row in range(self.rows):
                for column in range(self.columns):
                    self.data[row][column] += n.data[row][column]
        else:
            for row in range(self.rows):
                for column in range(self.columns):
                    self.data[row][column] += n
    
    @staticmethod
    def add_matrix(a, b):
        
        result = Matrix(a.rows, a.columns)

        for row in range(result.rows):
            for column in range(result.columns):
                result.data[row][column] = a.data[row][column] + b.data[row][column]
                    
        return result
    
    @staticmethod
    def subtract_matrix(a, b):
        
        result = Matrix(a.rows, a.columns)

        for row in range(result.rows):
            for column in range(result.columns):
                result.data[row][column] = a.data[row][column] - b.data[row][column]
                    
        return result

    def copy(self):

        new_matrix = Matrix(self.rows, self.columns)
        new_matrix.data = copy.deepcopy(self.data)
        return new_matrix

    def print(self):
        print(self.data)
