from Challenge_3 import Category

groceries = Category("Groceries")
clothes = Category("Clothes")
perfum = Category("Perfum")

groceries.deposit(100)
clothes.deposit(200)

clothes.get_balance()
groceries.get_balance()

groceries.transfer(groceries, 50, clothes)

clothes.get_balance()
groceries.get_balance()