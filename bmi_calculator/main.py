height = input("Enter height in meters e.g: 1.75 \n ")
weight = input("Enter weight in kilograms e.g: 65\n ")

height_int = float(height)
height_square = height_int**2
weight_int = float(weight)
bmi = weight_int/height_square
print(int(bmi))
