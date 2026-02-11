
def calculate_shipping_cost(weight, distance):
    # Function to calculate shipping cost based on weight and distance
    cost_per_kg = 2.5  
    cost_per_km = 1.0 
    return weight * cost_per_kg + distance * cost_per_km


def calculate_shipping_Tax(cost):
    # Function to calculate shipping tax based on cost
    tax_rate = 0.10  # 10% tax rate
    return cost * tax_rate

