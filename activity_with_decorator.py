def check_palindrome(func):
	def inner(words):
		pals = []

		for word in words:
			if word == word[::-1]:
				pals.append(word)

		return func(pals)
	return inner

@check_palindrome
def unique_chars_per_word(words):
	unique_chars = []

	for word in words:
		new_str = []
		[new_str.append(c) for c in word if c not in new_str]
		unique_chars.append(len(new_str))

	return unique_chars

@check_palindrome
def check_adjacent(words):
	lizt = []

	for word in words:
	
		dicts = {}
		x = 0
		while x < len(word) - 1:
			hold = word[x]

			count = 1
			repeat = hold

			for y in xrange(x + 1, len(word)):

				if hold == word[y]:
					count += 1
					repeat += word[y]
					x = y
				else:
					x += 1
					break

			if count > 1 and repeat not in dicts:
				dicts[repeat] = 1

				if dicts in lizt:
					lizt[lizt.index(dicts)][repeat]
				else:	
					lizt.append(dicts)
			elif count > 1 and repeat in dicts:
				dicts[repeat] += 1
	return lizt

print unique_chars_per_word(["racecar", "10010001001"])
print check_adjacent(["hahhah", "dood", "bbbaakkkaabbb"])
