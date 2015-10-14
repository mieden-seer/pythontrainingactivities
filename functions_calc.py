def calc(numbers, op):
	def mean(numbers):
		return float(sums(numbers)) / len(numbers)

	def sums(numbers):
		total = 0

		for num in numbers:
			total += num

		return total

	def median(numbers):
		numbers.sort()
		
		return numbers[len(numbers)/2]

	def maxim(numbers):
		maxi = 0;

		for num in numbers:
			if num > maxi:
				maxi = num

		return maxi

	def minim(numbers):
		mini = numbers[0]

		for num in numbers:
			if num < mini:
				mini = num

		return mini

	def count_elem(numbers, num):
		ctr = 0

		for x in numbers:
			if x == num:
				ctr += 1

		return ctr

	counts = []

	def count(numbers):
		for y in numbers:
			counts.append(count_elem(numbers, y))

	def mode(numbers):
		maxi = 0
		count(numbers)

		for z in counts:
			if z > maxi:
				maxi = z

		return numbers[counts.index(maxi)]

	calc_dict = {
		"min": minim,
		"max": maxim,
		"sum": sums,
		"median": median,
		"mean": mean,
		"mode": mode
	}

	return calc_dict[op](numbers)

result = calc([5,2,2,10,6], "mode")
print result
