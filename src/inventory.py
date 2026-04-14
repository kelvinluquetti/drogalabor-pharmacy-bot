class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f'Added {quantity} of {item_name}. Current stock: {self.items[item_name]}')

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f'Removed {quantity} of {item_name}. Remaining stock: {self.items[item_name]}')
            else:
                print(f'Unable to remove {quantity} of {item_name}. Not enough stock!')
        else:
            print(f'Item {item_name} does not exist in inventory.')

    def check_low_stock(self, threshold):
        low_stock_items = [item for item, quantity in self.items.items() if quantity <= threshold]
        if low_stock_items:
            print('Low stock alert for items:', low_stock_items)
        else:
            print('No items are below the low stock threshold.')

    def get_stock(self):
        return self.items
