class Bill:

	def __init__(self, amount):
		self._amount = amount

	def __str__(self):
		return 'A {}$ bill'.format(self._amount)

	def __repr__(self):
		return str(self._amount)

	def __int__(self):
		return int(self._amount)

	def __eq__(self, other):
		return self._amount == other.total()

	def __hash__(self):
	 	return hash(self._amount)

	def total(self):
		return self._amount

	

class BillBatch:

	def __init__(self, bills):
		self._bills = bills

	def __len__(self):
		return len(self._bills)

	def __getitem__(self, index):
		return self._bills[index]

	def total(self):
		return sum([int(bill) for bill in self._bills])



class CashDesk():

	def __init__(self):
		self._cash = []
		self._desk_info = {}

	def take_money(self, money):
		self._cash.append(money.total())

		if isinstance(money, Bill): #check whether money is Bill or BillBatch
			if str(money) not in self._desk_info:
				self._desk_info[str(money)] = 1
			else:
				self._desk_info[str(money)] += 1

		else:
			for bill in money:
				if str(bill) not in self._desk_info:
					self._desk_info[str(bill)] = 1
				else:
					self._desk_info[str(bill)] += 1

	def total(self):
		return sum(self._cash)

	def inspect(self):
		for item in self._desk_info.items():
			print(item)




a = Bill(10)
b = Bill(10)

money_holder = {}

if a in money_holder:
	money_holder[a] += 1
else:
	money_holder[a] = 1

if a in money_holder:
	money_holder[a] += 1
else:
	money_holder[a] = 1

print(money_holder)


values = [10, 20, 50, 100, 100]
bills = [Bill(value) for value in values]

print(bills)

batch = BillBatch(bills)

for bill in batch:
	print(bill)


print(batch.total())

desk = CashDesk()
desk.take_money(batch)

desk.inspect()
print(desk.total())

