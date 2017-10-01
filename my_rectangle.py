"""
hw-15
Abhishek Shekhar
"""
class rectangle(object):

    #constructor, instantiation method
    def __init__(self,length,width):

        self.length = length
        self.width = width
        

    def area(self):
        self.area = self.length*self.width
        return (self.area)

    def perimeter(self):
        self.perimeter =2*(self.length+self.width)
        return (self.perimeter)

    def set_length(self, input_length):

        self.length = input_length

    def set_width(self, input_width):

        self.width = input_width    
    
    def __add__(self,other):
        leng=(self.length+other.length)
        wid=(self.width+other.width)
        new_rectangle = rectangle(self.length,self.width)
        new_rectangle.set_length(leng)
        new_rectangle.set_width(wid)
        return (new_rectangle)
        
    def __str__(self):
        new= "length:"+str(self.length)+ "  "+"width:"+str(self.width)
        return new
      
    def __lt__(self, other):

        tmp_var = self.length < other.length
        tmp_var = self.width < other.width
        return tmp_var
    def __gt__(self, other):
        
        tmp_var = self.length > other.length
        tmp_var = self.width > other.width
        return tmp_var
    
    def __eq__(self, other):

        return  self.length == other.length and self.width == other.width

        



   
