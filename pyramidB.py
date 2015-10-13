def pyramidB(x):
	line = ""
	
	for num in xrange(0, x):
		space = ""
		one = ""

		for s in xrange(x - num):
			space += " "

		for o in xrange(num + 1):
			one += "1 "

		line = space + one
		print line

pyramidB(5)
