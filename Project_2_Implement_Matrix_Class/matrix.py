import math
from math import sqrt
import numbers

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
        if len(self) == 1:
            det = self[0][0]
        else:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            
            det = a*d-c*b
        
        return det
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace += self.g[i][i]
        return trace
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if len(self) == 1:
            inverse = [[1/self[0][0]]]
        else:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            
            k = a*d-b*c
            
            inverse = [[d/k, -b/k],[-c/k, a/k]]
            
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for c in range(len(self[0])):
            row = []
            for r in range(len(self)):
                row.append(self[r][c])
            transpose.append(row)
        return Matrix(transpose)
                             
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __len__(self):
        return self.h
    
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
        Sum = []
        for r in range(self.h):
            row =[]
            for c in range(self.w):
                row.append(self[r][c] + other[r][c])
            Sum.append(row)
        return Matrix(Sum)
                             
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
        Neg = []
        for r in range(self.h):
            row =[]
            for c in range(self.w):
                row.append(-self[r][c])
            Neg.append(row)
        return Matrix(Neg)
                             
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        Sub = []
        for r in range(self.h):
            row =[]
            for c in range(self.w):
                row.append(self[r][c] - other[r][c])
            Sub.append(row)
        return Matrix(Sub)
                             
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        Result = []
        if len(self[0]) != len(other):
            raise(ValueError, "These matrices cannot be multipled.")
                             
        for i in range(self.h):
            row = []
            for j in range(other.w):
                Sum = 0;
                for k in range(other.h):
                    Sum += self[i][k] * other[k][j]
                row.append(Sum)
            Result.append(row)
        return Matrix(Result)
                             
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
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
        Result = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                Result[i][j] = other*self[i][j]
        return Matrix(Result)
