"""
Finding the area of a rectangle, triangle, and circle


"""



def main():
    
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))
    radius = float(input("Please enter the radius of the circle: "))


    rectangle_area = (length * width)
    triangle_area = (0.5 * base * height)
    circle_area = (3.14 * (radius ** 2 ))
    
    print(f"The area of the {rectangle_area} is: ")
    print(f"The area of the {triangle_area} is: ")
    print(f"The area of the {circle_area} is: ")

main ()
