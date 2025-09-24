def area_rectangle(width, height):
    return width * height
def area_square(side):
    return side * side
def area_circle(radius):
    return 3.14 * radius * radius
_AREA_DISPATCH = {
    "rectangle": lambda x, y: area_rectangle(x, y),
    "square": lambda x, y: area_square(x),
    "circle": lambda x, y: area_circle(x),
}
def calculate_area(shape, x, y=0):
     key = str(shape).lower()
     try:
         func = _AREA_DISPATCH[key]
     except KeyError:
         raise ValueError(f"Unsupported shape: {shape}")
     return func(x, y)
if __name__ == "__main__":
     shape = input("Enter shape (rectangle/square/circle): ").strip().lower()
     try:
         if shape == "rectangle":
             x = float(input("Enter width: "))
             y = float(input("Enter height: "))
         elif shape == "square":
             x = float(input("Enter side: "))
             y = 0
         elif shape == "circle":
             x = float(input("Enter radius: "))
             y = 0
         else:
             print("Unsupported shape. Choose rectangle, square, or circle.")
             raise SystemExit(1)
     except ValueError:
         print("Invalid number entered.")
         raise SystemExit(1)

     try:
         area = calculate_area(shape, x, y)
         print(f"Area: {area}")
     except ValueError as err:
         print(err)