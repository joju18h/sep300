# George Paul Robert, Student ID: 117928226
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, operand):
        return self.x + operand.x, self.y + operand.y

    def __sub__(self, operand):
        return self.x - operand.x, self.y - operand.y

    def __mul__(self, num):
        return self.x * num, self.y * num

    def __truediv__(self, num):
        return round(self.x / num), round(self.y / num)

vector1 = Vector(10, 6)
vector2 = Vector(2, 3)

addition = vector1 + vector2
print("Addition: ", addition)

subtraction = vector1 - vector2
print("Subtraction: ", subtraction)

multiplication = vector1 * 2
print("Multiplication: ", multiplication)

division = vector1 / 2
print("Division: ", division)
