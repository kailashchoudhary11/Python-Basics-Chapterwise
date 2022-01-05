class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = f"{self.vec[0]}a0"

        for i in range (1, len(self.vec)):
            str1 += f" + {self.vec[i]}a{i}" 
        return str1

    def __add__(self, v):
        if len(self.vec) != len(v.vec):
            print("Addtion failed the length of both the vectors is not equal")
            return
        result = []
        for i in range(len(self.vec)):
            result.append(self.vec[i] + v.vec[i])
        return Vector(result)

    def __mul__(self, v):
        if len(self.vec) != len(v.vec):
            print("Multiplication failed as the length of both the vectors is not same")
            return
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * v.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)

v = Vector([2, 3])
print(len(v))

v1 = Vector([3, 5, 8])
print(len(v1))

v2 = Vector([9, 3, 8, 55])
print(len(v2))

v1 + v2
v1 * v2