class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__balance += amount
          return True
      else:
          return False

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__balance:
          self.__balance -= amount
          return True
      else:
          return False

  def get_balance(self):
      return self.__balance


def test_bank_account():
  account = BankAccount(12345678, "John Doe", 1000)
  print("Initial balance:", account.get_balance())

  account.deposit(500)
  print("After depositing 500:", account.get_balance())

  account.withdraw(200)
  print("After withdrawing 200:", account.get_balance())

  account.deposit(-500)
  print("After trying to deposit -500:", account.get_balance())

  account.withdraw(2000)
  print("After trying to withdraw 2000:", account.get_balance())


if __name__ == "__main__":
  test_bank_account()