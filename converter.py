def converter(inches, unit):
	if(unit == "km"):
		y = map(lambda x: x*0.0000254, inches)
	elif(unit == "m"):
		y = map(lambda x: x*0.0254, inches)
	elif(unit == "cm"):
		y = map(lambda x: x*2.54, inches)
	elif(unit == "feet"):
		y = map(lambda x: x*0.0833333, inches)
	elif(unit == "yard"):
		y = map(lambda x: x*0.0277778, inches)

	print y

converter((1,2,3,4,5), "cm")
