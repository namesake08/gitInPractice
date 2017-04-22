with open("config.xml", "r+") as r:
	for line in r:
		token = line[11:43]
	print(token)
