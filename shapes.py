###CSCI 4448 HW 1 Question 4 ###
###Steps: locate list of shapes in "database", open up list of shapes, sort list according to some rules (up to me), display individual shapes. ###
###print to console number of shapes in the database then have each shape "display itself" 
###Order shapes by number of sides in descending order 



class Shape:
    def __init__(self, num_sides, name):
        self.num_sides = num_sides
        self.name = name
        
    def display_self(self):
        print("A",self.name,"is being displayed")
        



def generate_shapes():
    db = []
    circle = Shape(0, 'Circle')
    triangle = Shape(3, 'Triangle')
    square = Shape(4, 'Square')
    
    db.append(circle)
    db.append(triangle)
    db.append(square)
    
    #order shapes based on descending number of sides 
    db.sort(key=lambda x: x.num_sides, reverse=True)
    return db 
    
    

###Main Program: Print number of shapes in database to console, have each shape display itself###

database = generate_shapes()

print("Number of shapes in database:", len(database))

for shape in database:
    shape.display_self()
