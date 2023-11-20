def max_calories_from_file(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

    # Split the data into separate inventories for each Elf
    elf_inventories = input_data.strip().split('\n\n')

    # Initialize a variable to keep track of the maximum calories
    max_calories = 0

    for elf in elf_inventories:
        # Calculate the total calories for each Elf
        # Sum up the calorie values, converting each line to an integer
        calories = sum(int(line)
                       for line in elf.splitlines() if line.isdigit())

        # Update max_calories if this Elf's total is greater
        max_calories = max(max_calories, calories)

    return max_calories


def total_calories_top_three(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

    elf_inventories = input_data.strip().split('\n\n')

    # List to store the total calories for each Elf
    all_calories = []

    for elf in elf_inventories:

        calories = sum(int(line)
                       for line in elf.splitlines() if line.isdigit())

        # Append the total calories of this Elf to the list
        all_calories.append(calories)

    # Calculate the sum of the top three highest calorie counts
    total_top_three = sum(sorted(all_calories, reverse=True)[:3])

    return total_top_three


# File containing the Elves' calorie data
file_path = 'elfcals.txt'

print("Max calories by a single Elf:", max_calories_from_file(file_path))

print("Total calories by top three Elves:",
      total_calories_top_three(file_path))
