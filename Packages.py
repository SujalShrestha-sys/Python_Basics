# can import in two ways


# 1. import the module
import Ecommerce.shipping

# 2. import the function
#from Ecommerce.shipping import calculate_shipping_cost



#Packages: a packages are a way to organize related modules together.


print("Shipping cost for 2kg and 10km is:",Ecommerce.shipping.calculate_shipping_cost(2,10))

print("Shipping tax for 2kg:", Ecommerce.shipping.calculate_shipping_Tax(2))


