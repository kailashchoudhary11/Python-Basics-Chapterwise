class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = f"{self.vec[0]}a0"

        for i in range (1, len(self.vec)):
            str1 += f" + {self.vec[i]}a{i}" 
        return str1

    def __add__(self, v):
        result = []
        for i in range(len(self.vec)):
            result.append(self.vec[i] + v.vec[i])
        return Vector(result)

    def __mul__(self, v):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * v.vec[i]
        return sum


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

sum = v1 + v2
print(sum)

dotProduct = v1 * v2
print(dotProduct)
