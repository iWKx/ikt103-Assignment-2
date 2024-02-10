def process_files(customers_file, products_file, orders_file):

  # Initialize empty dictionaries to store data
  customers = {}
  products = {}
  product_amounts = {}
  product_gross_income = {}
  customer_spending = {}

  # Process customers.csv
  with open(customers_file, 'r') as file:
    next(file)  # Skip the header row
    for line in file:
      id, name, address = line.strip().split(',')
      customers[int(id)] = {'name': name, 'address': address}
      print(f"Customer: {name}, {address}")

  # Process products.csv
  with open(products_file, 'r') as file:
    next(file)  # Skip the header row
    for line in file:
      id, name, price = line.strip().split(',')
      products[int(id)] = {'name': name, 'price': float(price)}
      print(f"Product: {name}, {price}")

  # Process orders.csv
  with open(orders_file, 'r') as file:
    next(file)  # Skip the header row
    for line in file:
      order_id, customer_id, product_id, amount = line.strip().split(',')
      customer_id = int(customer_id)
      product_id = int(product_id)
      amount = int(amount)

      # Update product amounts and gross income
      if product_id not in product_amounts:
        product_amounts[product_id] = 0
      product_amounts[product_id] += amount
      if product_id not in product_gross_income:
        product_gross_income[product_id] = 0
      product_gross_income[product_id] += amount * products[product_id]['price']

      # Update customer spending
      if customer_id not in customer_spending:
        customer_spending[customer_id] = 0
      customer_spending[customer_id] += amount * products[product_id]['price']

  # Print product amounts
  for product_id, amount in product_amounts.items():
    product_name = products[product_id]['name']
    print(f"{product_name} amount: {amount}")

  # Print product gross income
  for product_id, gross_income in product_gross_income.items():
    product_name = products[product_id]['name']
    print(f"{product_name} gross income: {gross_income}")

  # Print customer spending
  for customer_id, spending in customer_spending.items():
    customer_name = customers[customer_id]['name']
    print(f"{customer_name} money spent: {spending}")

# Replace with the actual file paths
process_files('customers.csv', 'products.csv', 'orders.csv')
