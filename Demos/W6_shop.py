def shop():
  items = {"Fish":1, "Eggs":1.99, "Chips":1.49, "Cheese":4, "Coconut":2.29, "Bread":1.39, "Nesquik":3.99, "Milk":1.59}
  return items

def view_all(products = {}):
  for i,j in products.items():
    print(f"{i}: £{j}")

def basket():
  b = []
  while True:
    item = input("Enter item (or \"stop\" to stop): ")
    if item.lower() == "stop":
      break
    else:
      n = int(input("Enter the quantity: "))
      for i in range(n):
        b.append(item)
  return b
def till(basket = []):
  shoplist = shop()
  total = 0.0
  for item in basket:
    total += shoplist[item]
  return total

def run():
  print("Welcome to Pete's shope - the best one ever. Please have a look around and add items that you like")
  chosen_items = basket()
  while True:
    print("Are you ready to pay for your items?")
    response = input()
    if response.lower() == "yes":
      to_pay = till(chosen_items)
      print(f"Pay £{to_pay} or i will call the cops")
      break
    else:
      chosen_items += basket()

run()
