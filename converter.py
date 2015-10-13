def converter(inches, unit):

	unit_dict = {
		"km": 0.0000254,
		"m": 0.0254,
		"cm": 2.54,
		"feet": 0.0833333,
		"yard": 0.0277778
	}

	y = map(lambda x: x*unit_dict[unit], inches)

	print y

converter((1,2,3,4,5), "cm")
