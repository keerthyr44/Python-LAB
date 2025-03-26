def calculate_triangle_area(base,height):
    area=0.5*base*height
    return area;
base=float(input("Enter the base of a triangle"))
height=float(input("Enter the height of triangle"))
area=calculate_triangle_area(base,height)

print(f"The Area of a triangle is:{area}")
