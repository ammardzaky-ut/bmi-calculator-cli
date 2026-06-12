
print("BMI Calculator")
print("=================")

berat = float(input("Enter your body weight (kg): "))
tinggi = float(input("Enter your body height (m): "))

bmi = berat / (tinggi * tinggi)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Your category is: Underweight")
elif 18.5 <= bmi < 25:
    print("Your category is: Normal weight")
elif 25 <= bmi < 30:
    print("Your category is: Overweight")
else:
    print("Your category is: Obesity")
# Program ini menghitung BMI berdasarkan berat dan tinggi yang dimasukkan oleh pengguna, kemudian memberikan kategori berdasarkan hasil BMI tersebut.   
