import math
from math import sqrt
import numbers
import matrix as m
import numpy as np

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
           
            return self.g[0][0]
        if self.h == 2:
            
            return self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
      
                     
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        # TODO - your code here
        summ=0
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if i == j:
                    summ+=self.g[i][j]
      
        return summ
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        
        det = Matrix.determinant(self)
        if len(self.g)==1 or len(self.g[0])==1:
            inverse.append([1/self.g[0][0]])
   
        if len(self.g)==2 or len(self.g[0])==2:
            inverse = ([self.g[1][1]/det,-1*self.g[0][1]/det],[-1*self.g[1][0]/det,self.g[0][0]/det])
        invers = m.Matrix(inverse)
        return invers

    def T(self):
            
            matrix_transpose = [[0 for y in range(len(self.g))]for x in range(len(self.g[0]))]
            #matrix_transpose = np.zeros((len(matrix[0]),len(matrix)))
         #matrix_transpose = []
        #     print(len(matrix))
        #     print(len(matrix[0]))
            for i in range(len(self.g)):
                for j in range(len(self.g[0])): 
                    matrix_transpose[j][i] = self.g[i][j]
            matrixTrans = m.Matrix(matrix_transpose)     
            return matrixTrans

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
              
        # initialize matrix to hold the results
        matrixSum = []

        # matrix to hold a row for appending sums of each element
        row = []

        # TODO: write a for loop within a for loop to iterate over
        # the matrices
        for i in range(len(self.g)):
            row=[]
            for j in range(len(self.g[0])):
        # TODO: As you iterate through the matrices, add matching
        # elements and append the sum to the row variable 
                row.append(self.g[i][j]+other.g[i][j])
        # TODO: When a row is filled, append the row to matrixSum. 
        # Then reinitialize row as an empty list
            matrixSum.append(row)
            matrixSummation = m.Matrix(matrixSum)
        return matrixSummation

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrixNeg = []

        # matrix to hold a row for appending sums of each element
        row = []

        # TODO: write a for loop within a for loop to iterate over
        # the matrices
        for i in range(len(self.g)):
            row=[]
            for j in range(len(self.g[0])):
        # TODO: As you iterate through the matrices, add matching
        # elements and append the sum to the row variable 
                row.append(-1*self.g[i][j])
        # TODO: When a row is filled, append the row to matrixSum. 
        # Then reinitialize row as an empty list
            matrixNeg.append(row)
            matrixNegative = m.Matrix(matrixNeg)
        return matrixNegative

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        # initialize matrix to hold the results
        matrixSub = []

        # matrix to hold a row for appending sums of each element
        row = []

        # TODO: write a for loop within a for loop to iterate over
        # the matrices
        for i in range(len(self.g)):
            row=[]
            for j in range(len(self.g[0])):
        # TODO: As you iterate through the matrices, add matching
        # elements and append the sum to the row variable 
                row.append(self.g[i][j]-other.g[i][j])
        # TODO: When a row is filled, append the row to matrixSum. 
        # Then reinitialize row as an empty list
            matrixSub.append(row)
            matrixSubtract = m.Matrix(matrixSub)
        return matrixSubtract
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        product = []
        current_rowA = []
        current_rowB = []
        Other = m.Matrix(other.g)
        transB = Other.T()
        row_results=[]
        for i in range(len(self.g)):
            for j in range(len(other.g[0])):
                result=0
                current_rowA=self.g[i]
                current_rowB=transB[j]
                for k in range(len(current_rowB)):
                    result += current_rowA[k]*current_rowB[k]
                row_results.append(result)
            product.append(row_results)
            row_results=[]
            matrixMul = m.Matrix(product)
        return matrixMul
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        matrixRmul = []

        # matrix to hold a row for appending sums of each element
        row = []

        # TODO: write a for loop within a for loop to iterate over
        # the matrices
        for i in range(len(self.g)):
            row=[]
            for j in range(len(self.g[0])):
        # TODO: As you iterate through the matrices, add matching
        # elements and append the sum to the row variable 
                row.append(other*self.g[i][j])
        # TODO: When a row is filled, append the row to matrixSum. 
        # Then reinitialize row as an empty list
            matrixRmul.append(row)
            matrixRmult = m.Matrix(matrixRmul)
        return matrixRmult
    
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            