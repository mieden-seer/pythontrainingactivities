def pyramidA(x):
	num_space = x - 1
	num_one = 1
	space = ""
	one = ""
	line = ""

	for num in xrange(1, x + 1):
		for s in xrange(num_space):
			space += " "

		for o in xrange(num_one):
			one += "1"

		line = space + one
		print line

		space = ""
		one = ""

		num_space -= 1
		num_one += 2

pyramidA(2)
