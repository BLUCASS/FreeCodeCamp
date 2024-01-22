from Challenge_4 import Rectangle, Square

rectangle = Rectangle(10, 5)
print(rectangle.get_area())
rectangle.set_height(3)
print(rectangle.get_perimeter())
print(rectangle)
rectangle.get_picture()

square = Square(9)
print(square.get_area())
square.set_side(4)
print(square.get_diagonal())
print(square)
square.get_picture()

rectangle.set_height(16)
rectangle.set_width(8)
rectangle.get_amount(square)