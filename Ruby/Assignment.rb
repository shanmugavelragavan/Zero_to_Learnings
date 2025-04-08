# 5: Banking Application
# Design a BankAccount class with private balance and transaction history, along with public interface methods. Create derived account types (SavingsAccount, CheckingAccount, FixedDeposit) that inherit core banking functionality while adding specific features like interest calculations or transaction fees.


# Class for Bank Account
class BankAccount
  def initialize(account_holder, balance = 0)
    @account_holder = account_holder
    @balance = balance
    @transactions = []
  end

  # Deposit method
  def deposit(amount)
    if amount > 0
      @balance += amount
      @transactions << "Deposited: ₹#{amount}"
    else
      puts "Error: Deposit amount must be positive."
    end
  end

  # Withdraw method
  def withdraw(amount)
    if amount > 0 && amount <= @balance
      @balance -= amount
      @transactions << "Withdrew: ₹#{amount}"
    else
      puts "Error: Insufficient funds or invalid amount."
    end
  end

  # Get balance
  def get_balance
    @balance
  end

  # Get transaction history
  def get_transaction_history
    @transactions.clone
  end
end

# Savings Account with Interest Calculation
class SavingsAccount < BankAccount
  def initialize(account_holder, balance = 0, interest_rate = 0.05)
    super(account_holder, balance)
    @interest_rate = interest_rate
  end

  def calculate_interest
    interest = @balance * @interest_rate
    deposit(interest)
    interest
  end
end

# Checking Account with Transaction Fee
class CheckingAccount < BankAccount
  def initialize(account_holder, balance = 0, transaction_fee = 10)
    super(account_holder, balance)
    @transaction_fee = transaction_fee
  end

  def withdraw(amount)
    total_amount = amount + @transaction_fee
    if total_amount <= @balance
      super(amount)
      super(@transaction_fee)
    else
      puts "Error: Insufficient funds to cover withdrawal and transaction fee."
    end
  end
end

# Fixed Deposit Account with Maturity Interest
class FixedDeposit < BankAccount
  def initialize(account_holder, balance = 0, interest_rate = 0.08, duration_months = 12)
    super(account_holder, balance)
    @interest_rate = interest_rate
    @duration_months = duration_months
    @locked = true
  end

  def mature
    if @locked
      @locked = false
      maturity_amount = @balance * (1 + @interest_rate)
      deposit(maturity_amount)
      maturity_amount
    else
      puts "FD has already matured!"
    end
  end
end


if __FILE__ == $0  
  # Creating a Savings Account
  savings = SavingsAccount.new("Shanmugavel", 5000)
  interest = savings.calculate_interest
  puts "Interest Earned: ₹#{interest}"
  puts "Savings Account Transactions: #{savings.get_transaction_history}"

  # Creating a Checking Account
  checking = CheckingAccount.new("Shanmugavel", 3000)
  checking.withdraw(500)
  puts "Checking Account Transactions: #{checking.get_transaction_history}"

  # Creating a Fixed Deposit Account
  fd = FixedDeposit.new("Shanmugavel", 10000)
  puts "FD Maturity Amount: ₹#{fd.mature}"
  puts "Fixed Deposit Transactions: #{fd.get_transaction_history}"
end
