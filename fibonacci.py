#1 1 2 3 5

def fibo(x):
	temp = 0
	a = 1
	b = 0

	for n in xrange(x):
		temp = a
		a = temp + b
		b = temp

		yield temp

for i in fibo(5):
	print i
