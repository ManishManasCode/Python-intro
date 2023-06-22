def rev_string_dectorator(func):
    def wrapper():
        val=func()
        return val[::-1]
    return wrapper

@rev_string_dectorator
def say_string_world():
    return "Hello World"

print(say_string_world())

