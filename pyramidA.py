def pyramidA(x):
	space = ""
	one = ""
	line = ""

	for num in xrange(0, x):

		for s in xrange(x - num):
			space += " "

		for o in xrange(num + num + 1):
			one += "1"

		line = space + one
		print line

		space = ""
		one = ""

pyramidA(5)
