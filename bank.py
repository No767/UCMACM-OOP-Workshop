class Bank:
    def __init__(self):
        self._users = {}
        
    def add_user(self, user):
        self._users[user] = {"balance": 0}
        print("Added " + user)
        
    def get_user(self, user):
        return self._users[user]
    
    def edit_user_balance(self, user, amount):
        self._users[user]["balance"] = amount
        
    def show_users(self):
        for idx, item in enumerate(self._users, start=1):
            print(f"{idx}: {item}")
            
class User(Bank):
    def __init__(self, name, balance = 0):
        super().__init__()
        super().add_user(name)
        self._name = name
        self._balance = balance
        
    def show_user(self):
        current_user = super().get_user(self._name)
        user_balance = current_user["balance"]
        print(f"Name: {self._name}, Balance: {user_balance}")
        
    def update_balance(self, amount):
        name = self._name
        super().edit_user_balance(name, amount)
        
bank = Bank()

bank.add_user("Noelle")
bank.show_users()

# # What happens if now the user attribute is edited?
# Comment out the two lines of code below to find out
# bank.users = 0
# bank.show_users()

# Creating the child class
user = User("Jack", 0)
user.show_user()

# Default balance is 0, so let's update it
user.update_balance(50)
user.show_user()