def calculate_fuel_for_fuel(current_total, mass): 
    fuel = (mass // 3) - 2 
    if fuel <= 0:
        return current_total
    else:
        return calculate_fuel_for_fuel(current_total + fuel, fuel)
        
def calculate_fuel(mass):
    fuel_for_module = (mass // 3) - 2
    fuel_for_fuel = calculate_fuel_for_fuel(0, fuel_for_module)
    return fuel_for_module + fuel_for_fuel

with open('../aoc_inputs/2019/day01_input.txt', "r") as f:
    masses = f.read().splitlines()
    fuel_total = sum(calculate_fuel(int(mass)) for mass in masses)
    print(fuel_total)
