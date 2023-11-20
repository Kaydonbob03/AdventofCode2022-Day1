def max_calories_from_file(file_path):

    with open(file_path, 'r') as file:
        input_data = file.read()

    elf_inventories = input_data.strip().split('\n\n')

    max_calories = 0

    for elf in elf_inventories:
        calories = sum(int(line)
                       for line in elf.splitlines() if line.isdigit())

        max_calories = max(max_calories, calories)

    return max_calories


file_path = 'elfcals.txt'
print(max_calories_from_file(file_path))
