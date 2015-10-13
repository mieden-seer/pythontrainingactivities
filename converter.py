def converter(inches, unit):

	units = ('km','m','cm','feet','yard')
	nums = (0.0000254, 0.0254, 2.54, 0.0833333, 0.0277778)

	y = map(lambda x: x*nums[units.index(unit)], inches)

	print y

converter((1,2,3,4,5), "km")
