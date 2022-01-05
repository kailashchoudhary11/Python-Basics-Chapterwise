class C2DVector:

    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return f"{self.i}i + {self.j}j"

class C3DVector(C2DVector):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        # return f"{self.i}i + {self.j}j + {self.k}k"
        return super().__str__() + f" + {self.k}k"
        
# Creating 2d vector
v2d = C2DVector(1, 3)
print(v2d)

# Creating 3d vector
v3d = C3DVector(1, 9, 7)
print(v3d)
