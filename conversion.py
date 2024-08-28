# Define variables for pound (lb) values
lb_value_1 = 12.5
lb_value_2 = 25
lb_value_3 = 37.5
lb_value_4 = 50
lb_value_5 = 62.5

# Coversion factor: pound (lb) = kilogram (kg) * 2.20462
conversion_factor = 11.0231

# Calculate kilogram (kg) for each pound (lb) value
kilogram_1 = lb_value_1 / conversion_factor
kilogram_2 = lb_value_2 / conversion_factor
kilogram_3 = lb_value_3 / conversion_factor
kilogram_4 = lb_value_4 / conversion_factor
kilogram_5 = lb_value_5 / conversion_factor

# Output the results
print(f"{lb_value_1} pounds is equal to {kilogram_1:.2f} kilograms.")
print(f"{lb_value_2} pounds is equal to {kilogram_2:.2f} kilograms.")
print(f"{lb_value_3} pounds is equal to {kilogram_3:.2f} kilograms.")
print(f"{lb_value_4} pounds is equal to {kilogram_4:.2f} kilograms.")
print(f"{lb_value_5} pounds is equal to {kilogram_5:.2f} kilograms.")
