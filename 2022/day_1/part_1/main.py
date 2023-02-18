def get_data():
	with open("input.txt") as f:
		return f.readlines()


def format_data(data):
	elves = []
	elf = []

	for line in data:
		if line == '\n':
			elves.append(elf)
			elf = []
		else: elf.append(int(line))

	return elves


def count_calories(elves):
	return [sum(elf) for elf in elves]


def main():
	data = get_data()
	elves = format_data(data)
	elf_calories = count_calories(elves)
	top_elf = max(elf_calories)
	print(top_elf)


if __name__ == "__main__":
	main()