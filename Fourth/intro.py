class Greeting:
    name=""
    def __init__(self,name):
        print("Constructor is envoked")
        self.name=name

    def say_hello_wrold(self):
        print('Hello World')
    def say_hello(self,name):
        print(f"Hello,{name}")

    def say_hello_name(self):
        print(f"Hello,{self.name}")
    def __str__(self):
        return "This is a Greet Class"

obj= Greeting("Mark")
obj.say_hello_name()
# obj.say_hello_name()
#print(obj.name)
# obj.say_hello("Jhon")
# obj = Greeting()
# obj.say_hello_wrold()