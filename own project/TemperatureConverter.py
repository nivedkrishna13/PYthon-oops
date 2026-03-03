class TemperatureConverter():
    @staticmethod
    def C_to_F(C):
        return (C * 9/5) + 32
    @staticmethod
    def F_to_C(F):
        return (F - 32) * 5/9
    
temp_C = float(input("Enter temperature in Celsius: "))
temp_F = TemperatureConverter.C_to_F(temp_C)
print(f"{temp_C} degrees Celsius is equal to {temp_F} degrees Fahrenheit.")