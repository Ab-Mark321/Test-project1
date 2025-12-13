# Rectangle Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width    
        self.height = height  
        
        
rect = Rectangle(5, 10)
print(f"Rectangle width: {rect.width}")
print(f"Rectangle height: {rect.height}")
print(f"Area: {rect.width * rect.height}")  


print(f"Area : {Rectangle(3, 7).width * Rectangle(3, 7).height}") #alternative method