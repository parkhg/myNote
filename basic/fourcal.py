# Class 정의

class Cal4:
    def __init__(self, v1, v2):
        self.first = v1
        self.second = v2
    def setdata(self, v1, v2):
        self.first = v1
        self.second = v2
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    @property
    def div(self):
        if self.second == 0:
            result = 0
        else:
            result = self.first / self.second
        return result



a = Cal4(4,3)

print("SUM : ", a.sum())
print("MUL : ", a.mul())
print("SUB : ", a.sub())
print("DIV : ", a.div)
