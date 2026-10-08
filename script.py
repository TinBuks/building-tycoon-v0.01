import time

player_money = 5000
profit = 0

def generate_income(income, upkeep, interval=2):
    profit = income - upkeep
    print(f"Waiting {interval} seconds for profit...")
    time.sleep(interval)
    return profit

my_buildings = []

def purchase_building(name, cost, profit):
  global player_money
  if player_money >= cost:
    player_money -= cost
    my_buildings.append({"name": name, "profit": profit})
    print(f"Bought {name}! Remaining money: ${player_money}")
  else:
    print("You don't have enough money for this building.")

buildings_to_buy = [("Small House", 100, 30), ("Medium House", 250, 90), ("Large House", 600, 250)]

while True:
  while True:
    choice = input("Enter building to buy (Small House, Medium House, Large House) or 'quit': ")
    if choice.lower() == 'quit':
      break
    for name, cost, profit in buildings_to_buy:
      if name.lower() == choice.lower():
        purchase_building(name, cost, profit)
  total_profit = sum(b["profit"] for b in my_buildings)
  earned = generate_income(total_profit, upkeep=0)
  player_money += earned
  print(f"Total money: {player_money}")
  print(f"Profit this month: {earned}")   
