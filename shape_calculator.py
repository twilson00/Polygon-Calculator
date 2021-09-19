class Rectangle:

    def __init__(self, width, height):
        self._height = height
        self._width = width
        
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._height * self._width

    def get_perimeter(self):
        return 2 * self._width + 2 * self._height
    
    def get_diagonal(self):
        return (self._width ** 2 + self._height ** 2) ** .5

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        
        picture = ""
        for i in range(0, self._height):
            picture += "*" * self._width + "\n"
            
        return picture
    
    def get_amount_inside(self, rectangle):
        outsideArea = self.get_area()
        insideArea = rectangle.get_area()
        
        return outsideArea // insideArea


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
        
    def __str__(self):
        return f"Square(side={self._width})"
        
    def set_side(self, length):
        self._height = length
        self._width = length
