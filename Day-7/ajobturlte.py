import turtle

class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, pixel):
        super().right(pixel)

    def right(self, pixel):
        print("I won't turn right, because I am Ajob!!")

if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.right(50)
    turtle.done()