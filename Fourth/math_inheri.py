class MathFunction:

    def sum(self,a,b):
        return a+b
    
    def product(self , a, b):
        return a*b
    
    def sub(self,a,b):
        return a-b
    
    def div(self,a,b):
        return a/b

class MathFormulas(MathFunction):
#(a+b)**2 
    def method1(self, a, b):
        return self.product(
            self.sum(a,b),
            self.sum(a,b)
        )

obj=MathFormulas()
print(obj.method1(2,3))
# obj=MathFunction(5,2)
# print