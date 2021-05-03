class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Add product to", self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = "Natchanon"
customer1.lastName = "L"

customer2 = Customer()
customer2.name = "Apiluck"
customer2.lastName = "P"

customer3 = Customer()
customer3.name = "Nichapat"
customer3.lastName = "l"

customer1.addCart()
customer2.addCart()
customer3.addCart()