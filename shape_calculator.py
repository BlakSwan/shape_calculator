class Rectangle(object):
    def __init__(self,width,height,*args):
        self.width = width
        self.height = height
        self.inside_shape = args
    
    def __repr__(self):
        if self.width != self.height:
            return f'Rectangle(width={self.width}, height={self.height})'
        else:
            return f'Square(side={self.width})'
        
    def set_width(self, width):
        self.width = width
        if isinstance(self, Square):
            self.height = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        
    def get_picture(self):
        picture = ''
        if self.width > 50:
            return "Too big for picture."
        for i in range(self.height):
            for x in range(self.width):
                picture = picture + '*'
            picture = picture + '\n'
        return picture
        
    def get_amount_inside(self, other):
        if other.width <= self.width and other.height <= self.height:
            cols = self.width // other.width
            rows = self.height // other.height
            return cols * rows
        return 0

class Square(Rectangle):
    def __init__(self, side, *args):
        self.width = side
        self.height = side
  
        
    def set_side(self, side):
        self.width = side
        self.height = side
    
