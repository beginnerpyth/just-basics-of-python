class mam:
    def __init__(self,age,score):
        self.age=age
        self.score=score

    def greet(self):
        return f"he is {self.age} and he got {self.score}"


object1= mam(12,33)
object2 = mam(12,22)
h = object1.greet()
print(h)

