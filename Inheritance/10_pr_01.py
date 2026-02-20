# Create a class C-2d vector and use it to create another class representing a 3-d vector.
# Create a class C-2d vector and use it to create another class representing a 3-d vector.
class c2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        if self.jcap >= 0:
            return f"{self.icap}i + {self.jcap}j"
        else:
            return f"{self.icap}i - {-self.jcap}j"
        
class c3dVec(c2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        if self.jcap >= 0:
            return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
        else:
            return f"{self.icap}i - {-self.jcap}j - {-self.kcap}k"

v2d = c2dVec(1, -2)
print(f"The 2d vector is: {v2d}")

v3d = c3dVec(-1, -2, -6)
print(f"The 3d vector is: {v3d}")




        