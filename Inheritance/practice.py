class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} "
            index += 1
        return str1

    def __add__(self,vec1):
        if len(self.vec) != len(vec1.vec):
            raise ValueError("Vector dimensions have to be equal.")
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec1.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec1):
        if len(self.vec) != len(vec1.vec):
            raise ValueError("Vector dimensions have to be equal.")
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec1.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)
    
v1 = Vector([1, 2, 4, 6, 2])
v2 = Vector([2, 5, 6, 7, 9])

try:
    v3 = v1 + v2
    print(f"The sum of two vectors are: {v3}")
except ValueError as e:
    print(f"Error occur: {e}")

try:
    v4 = v1 * v2
    print(f"The multiplication of two vectors are: {v4}")
except ValueError as e:
    print(f"Error occur: {e}")

print(len(v1))
print(len(v2))