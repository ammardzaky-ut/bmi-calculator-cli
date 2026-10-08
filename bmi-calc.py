class BMICalculator:
    def __init__(self, weight: float, height_cm: float):
        self.weight = weight
        self.height_m = height_cm / 100  # konversi cm ke meter

    def calculate(self) -> float:
        return round(self.weight / (self.height_m ** 2), 2)

    def category(self) -> str:
        bmi = self.calculate()
        if bmi < 18.5:
            return "Kurus"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Gemuk"
        else:
            return "Obesitas"


def main():
    print("=== BMI Calculator ===")
    try:
        user_weight = float(input("Masukkan berat badan (kg): "))
        user_height = float(input("Masukkan tinggi badan (cm): "))

        if user_weight <= 0 or user_height <= 0:
            print("Error: Berat dan tinggi harus lebih dari 0.")
            return

        calc = BMICalculator(user_weight, user_height)
        print(f"BMI kamu: {calc.calculate()} ({calc.category()})")

    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka.")


if __name__ == "__main__":
    main()