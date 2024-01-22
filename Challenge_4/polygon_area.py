class Rectangle:

    def __init__(self, width=1, height=1) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f'Rectangle (width={self.width}, height={self.height})'

    def set_height(self, height) -> None:
        self.height = height
    
    def set_width(self, width) -> None:
        self.width = width

    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self) -> float:
        return (((self.width ** 2) + (self.height ** 2)) ** 0.5)

    def get_picture(self) -> None:
        if self.height < 50 and self.width < 50:
            for c in range(0, self.height):
                print('*' * self.width)
        else:
            print('Too big for the picture.')

    def get_amount(self, shape) -> None:
        if self.height > shape.height:
            x = self.height // shape.height
            print(f'You can fit {x} times vertically')
            if self.width > shape.width:
                y = self.width // shape.width
                print(f'You can fit {y} times horizontally')
        elif self.width > shape.width:
            y = self.width // shape.width
            print(f'You can fit {y} times')
            if self.height > shape.height:
                x = self.height // shape.height
                print(f'You can fit {x} times vertically')
        else:
            print('The figure is too big to fit.')

class Square(Rectangle):

    def __init__(self, side=1) -> None:
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f'Square (side={self.height})'

    def set_side(self, side) -> None:
        super().__init__(side, side)