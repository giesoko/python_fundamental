"""
All basic syntax in a programming language consists of:
1. sequential,
2. branch,
3. repetition
"""
# sequential
print('mom said "Go to the shop"')
print('Budi answered "Okay, what should I buy?"')
print('mom said "Buy a bottle of milk. If they had eggs, buy 6"')
print('"Sure!", so Budi went to the shop')
print('and started shopping')

# branching
milk_bottle_count = int(input("Enter count of milk available in the shop: "))

if milk_bottle_count > 0:
    Egg_avail = input("Did the shop have eggs? Enter yes or no: ")
    if Egg_avail == "yes":
        if milk_bottle_count == 6:
            print('Budi bought 6 bottle of milk')
        elif milk_bottle_count > 6:
            print('Budi bought 6 bottles of milk')
        else:
            print('Budi bought 1 bottle of milk')
    else:
        print('Budi bought 1 bottle of milk')

else:
    print('Budi did not buy any milk')
print('Budi went home')