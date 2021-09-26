class Rectangle:
    def __init__(self, width,height):
        self.height =height
        self.width = width
    def __str__(self):
         return f'{type(self).__name__}(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * self.width + 2* self.height

    def get_diagonal(self):
        import math
        return math.sqrt(pow(self.width, 2)+ pow(self.height, 2))

    def get_picture(self):
        if (self.width<=50 and self.height<=50):
            horizontal  = "*"*self.width
            store =[]
            for i in range(self.height):
                store.append(horizontal)
            shape  = "\n".join(store)
            return shape +"\n"
        if (self.width > 50 or self.height>50):
            return "Too big for picture."
    def get_amount_inside(self,shape):
        area_within =shape.get_area()
        bigger_area =self.get_area()
        return bigger_area//area_within
        

    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f'{type(self).__name__}(side={self.width})'
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)