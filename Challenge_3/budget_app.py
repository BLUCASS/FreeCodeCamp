class Category:

    def __init__(self, name: str) -> None:
        self.ledger = []
        self.name = name
        self.total = 0

    def deposit(self, amount) -> None:
        description = 'Deposit'
        data = {"amount": amount, "description": description}
        self.ledger.append(data)
        self.total = amount
    
    def withdraw(self, category) -> bool:
        amount = int(input('Enter the amount to withdraw: '))
        description = str(input('Enter the description: ')).capitalize()
        if self.check_funds(category, amount):
            data = {"amount": amount, "description": description}
            self.total -= amount
            self.ledger.append(data)
            return True
        else:
            return False
        
    def get_balance(self) -> str:
        print(f'{self.name:*^50}')
        for c in self.ledger:
            print(f'{c["description"]:<40}{c["amount"]:>10}')
        print(f'\n{"Total":<40}{self.total:>10}')

    def transfer(self, origin, amount, destiny) -> None:
        if self.check_funds(origin, amount):
            description = f'Transfer from {origin.name}'
            data = {"amount": amount, "description": description}
            destiny.ledger.append(data)
            destiny.total += amount
            description = f'Transfer to {destiny.name}'
            data2 = {"amount": amount, "description": description}
            origin.ledger.append(data2)
            origin.total -= amount

    def check_funds(self, category, value) -> bool:
        if category.total > value: return True
        return False
