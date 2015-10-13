def build_half_triangle(x):
	line = ""

	for num1 in xrange(1, x + 1):
		for num2 in xrange(0, num1):
			line += "1"

		print line
		line = ""

build_half_triangle(4)
