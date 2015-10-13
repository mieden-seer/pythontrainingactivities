s = "door broom mice"

split_word = s.split()
new_word = ""
new_str = []

for word in split_word:
	[new_str.append(c) for c in word if c not in new_str]
	new_word += "".join(new_str)
	new_word += " "
	new_str = []

print new_word
