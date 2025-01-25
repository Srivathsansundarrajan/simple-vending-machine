class Product:

    def __init__(self, name, price, quantity, weight):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight

    def __str__(self):
        return f"{self.name}: Price: {self.price}, Quantity: {self.quantity}, Weight: {self.weight}g"


class Shop:

    def __init__(self):
        self.products = {}
        self.cart = {}
        self.purchase_history = {}

    def add_product(self, name, price, quantity, weight):
        self.products[name] = Product(name, price, quantity, weight)

    def edit_product(self, name, new_price=None, new_quantity=None):
        if name in self.products:
            if new_price is not None:
                self.products[name].price = new_price
            if new_quantity is not None:
                self.products[name].quantity += new_quantity
        else:
            print("Product not found.")

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
        else:
            print("Product not found.")

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(product)

    def purchase_summary(self):
        print("\nPurchase History:")
        for customer, purchases in self.purchase_history.items():
            print(f"{customer}:")
            for product, quantity in purchases.items():
                print(f"  {product}: {quantity} units")


class Admin:

    def __init__(self, shop):
        self.shop = shop

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Purchase History")
            print("5. Exit Admin Mode")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter product name: ")
                price = int(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                weight = int(input("Enter product weight (g): "))
                self.shop.add_product(name, price, quantity, weight)
            elif choice == 2:
                name = input("Enter product name to edit: ")
                new_price = input("Enter new price (or leave blank): ")
                new_quantity = input(
                    "Enter new quantity to add (or leave blank): ")
                self.shop.edit_product(
                    name,
                    int(new_price) if new_price else None,
                    int(new_quantity) if new_quantity else None,
                )
            elif choice == 3:
                name = input("Enter product name to delete: ")
                self.shop.delete_product(name)
            elif choice == 4:
                self.shop.purchase_summary()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Try again.")


class Customer:

    def __init__(self, shop):
        self.shop = shop

    def customer_menu(self):
        name = input("Enter your name: ")
        cart = {}
        temp_reduction = {}

        while True:
            print("\nCustomer Menu:")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Checkout")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.shop.display_products()
            elif choice == 2:
                product_name = input("Enter product name to add to cart: ")
                if product_name in self.shop.products:
                    quantity = int(input("Enter quantity: "))
                    product = self.shop.products[product_name]

                    if product.quantity >= quantity:
                        cart[product_name] = cart.get(product_name,
                                                      0) + quantity
                        product.quantity -= quantity
                        temp_reduction[product_name] = temp_reduction.get(
                            product_name, 0) + quantity
                    else:
                        print("Not enough stock available.")
                else:
                    print("Product not found.")
            elif choice == 3:
                total = 0
                print("\nYour Cart:")
                for product_name, quantity in cart.items():
                    product = self.shop.products[product_name]
                    print(
                        f"{product_name}: {quantity} units @ {product.price} each"
                    )
                    total += product.price * quantity

                print(f"Total: {total}")
                confirm = input("Confirm purchase? (yes/no): ")
                if confirm.lower() == "yes":
                    self.shop.purchase_history[name] = cart
                    temp_reduction.clear()
                    print("Purchase successful!")
                    break
                else:
                    print("Purchase not confirmed. Returning to menu.")

            elif choice == 4:

                for product_name, quantity in temp_reduction.items():
                    self.shop.products[product_name].quantity += quantity
                print("Cart cleared. Quantities restored.")
                break

            else:
                print("Invalid choice. Try again.")


def main():
    shop = Shop()
    admin = Admin(shop)
    customer = Customer(shop)

    # Adding initial products
    shop.add_product("garlic_powder", 90, 10, 250)
    shop.add_product("blackpepper", 150, 20, 200)
    shop.add_product("cinnamon", 40, 10, 150)
    shop.add_product("cardamon", 60, 15, 150)
    shop.add_product("cumin", 100, 25, 250)
    shop.add_product("cloves", 29, 10, 50)

    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        role = int(input("Enter your choice: "))

        if role == 1:
            admin.admin_menu()
        elif role == 2:
            customer.customer_menu()
        elif role == 3:
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
