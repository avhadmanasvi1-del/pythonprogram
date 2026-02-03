
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    area = 3.14 * r * r
    print("Area of Circle:", area)

elif choice == 2:
    l = float(input("Enter length of rectangle: "))
    b = float(input("Enter breadth of rectangle: "))
    area = l * b
    print("Area of Rectangle:", area)

elif choice == 3:
    b = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    area = 0.5 * b * h
    print("Area of Triangle:", area)

else:
    print("Invalid choice")
