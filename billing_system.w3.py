class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


class Bill:

    def __init__(self):
        self.products = []
        self.tax_rate = 5

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.calculate_total()

        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):

        print("\n==============================")
        print("          FINAL BILL")
        print("==============================")

        print(
            f"{'Product':<20}"
            f"{'Price':<10}"
            f"{'Quantity':<10}"
            f"{'Total':<10}"
        )

        print("-" * 50)

        for product in self.products:
            total = product.calculate_total()

            print(
                f"{product.name:<20}"
                f"{product.price:<10.2f}"
                f"{product.quantity:<10}"
                f"{total:<10.2f}"
            )

        print("-" * 50)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':<40}{subtotal:.2f}")
        print(f"{'Tax (5%)':<40}{tax:.2f}")
        print(f"{'Final Total':<40}{total:.2f}")

        print("==============================")


# Create products
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 1000, 2)
product3 = Product("Keyboard", 2000, 1)

# Create bill
bill = Bill()

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display final bill
bill.display_bill()