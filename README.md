# Vending Machine System

This **Vending Machine System** is a Python-based application that provides an interactive interface for managing and purchasing products. The system supports both **Admin** and **Customer** roles, allowing for seamless product management and shopping experiences.

---

## Features

### Admin Features
- **Add Products**: Add new products to the vending machine inventory.
- **Edit Products**: Update the price or quantity of existing products.
- **Delete Products**: Remove products from the inventory.
- **View Purchase History**: Track customer purchase details.

### Customer Features
- **View Products**: Browse available products with price, quantity, and weight details.
- **Add to Cart**: Add products to the shopping cart with the desired quantity.
- **Checkout**: View the cart, total cost, and confirm purchases.
- **Cart Management**: Cart quantities are restored if the purchase is canceled.

### Additional Features
- **Inventory Management**: Real-time inventory updates upon adding to or removing from the cart.
- **Purchase History Tracking**: Keeps a record of customer purchases.
- **Preloaded Products**: The system starts with a predefined set of products.

---

## How to Run

1. **Clone the Repository**:
   
   git clone https://github.com/<your-username>/vending-machine.git
   cd vending-machine

2. **Run the Application: Ensure you have Python 3 installed. Execute the following command**:



    python vending_machine.py

    Select Role:

    Choose between Admin and Customer roles from the main menu.

    Follow the prompts to perform desired actions.
   
## Code Overview
### Main Components
#### Product Class:

  - Represents individual products with attributes: name, price, quantity, and weight.
  Provides a string representation for easy display.
  ---
#### Shop Class:

  - Manages the product inventory and purchase history.
  Provides methods for adding, editing, deleting, and displaying products.
---
#### Admin Class:

- Handles product management through an admin menu interface.
 Interacts with the Shop class for inventory updates.
---
#### Customer Class:

- Allows customers to browse products, add to cart, and checkout.
Manages cart operations and interacts with the Shop class for inventory updates.

#### Main Function:

- Serves as the entry point for the application.
- Allows users to select between Admin and Customer modes.
- Preloaded Products

The system starts with the following products:

- Product	Price (₹)	Quantity	Weight (g)
- Garlic Powder	90	10	250
- Black Pepper	150	20	200
- Cinnamon	40	10	150
- Cardamom	60	15	150
- Cumin	100	25	250
- Cloves	29	10	50

# Sample Usage

## Example Interaction

### Main Menu:


Main Menu:
1. Admin
2. Customer
3. Exit
Enter your choice: 1

Admin Menu:
1. Add Product
2. Edit Product
3. Delete Product
4. View Purchase History
5. Exit Admin Mode
Enter your choice: 1

Customer Menu:
1. View Products
2. Add to Cart
3. Checkout
4. Exit
Enter your choice: 2
---
# Future Enhancements

- Database Integration: Store product and purchase data in a database.
- GUI Support: Implement a graphical user interface for better usability.
- Payment System: Add options for payment through credit cards, wallets, or UPI.
- Discounts and Offers: Include promotional discounts or combo offers

