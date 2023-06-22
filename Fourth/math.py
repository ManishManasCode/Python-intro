class MathFunction:
    a=None
    b=None

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b
    
    def product(self):
        return self.a*self.b
    
    def sub(self):
        return self.a-self.b
    
    def div(self):
        return self.a/self.b
    
# obj=MathFunction(5,2)
# print(obj.sum())
# print(obj.product())
# print(obj.sub())
# print(obj.div())