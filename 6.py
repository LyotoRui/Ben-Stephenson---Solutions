bill = float(input('Enter cost: '))
bill = bill.__round__(2)
tax = float(bill * 0.195).__round__(2)
tips = float(bill * 0.18).__round__(2)
total = bill + tax + tips
print(f'Bill: ${bill}\nTax: ${tax}\nTips: ${tips}\n-----\nTotal: ${total}')