class Restaurant:
    def __init__(self, name, cusine, menu):
        self.name = name
        self.price = cusine
        self.quantity = menu


class FastFood(Restaurant):
    def __init__(self, name, cusine, menu, drive_thru):
        super().__init__(name, cusine, menu)
        self.drive_thru = drive_thru
    def order(self, dish_name, quantity):
        if dish_name in menu:
            menu_quantity = menu[dish_name]['quantity']
            if quantity <= menu_quantity:
                total_cost = menu[dish_name]['price']*quantity
            else:
                return Exception(f"We have just {menu_quantity} portions of {dish_name}. Requested quantity is not available.")        
            return total_cost
        return Exception(f"{dish_name} is not available.")        

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available