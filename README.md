# AdventofCode2022-Day1


## Elves Calorie Tracker

This repository contains Python scripts designed to analyze the calorie intake of Santa's Elves during their expedition. The scripts provide solutions for two specific tasks:

1. **Finding the Elf with the Maximum Calorie Intake**: Identifies which Elf is carrying the most calories in their food supply.
2. **Calculating Total Calories of Top Three Elves**: Determines the combined calorie count of the three Elves carrying the most calories.

## How it Works

The repository includes two main functions:

### `max_calories_from_file(file_path)`

- **Purpose**: This function reads a text file containing the calorie counts for various food items carried by each Elf. It calculates and returns the maximum total calories carried by a single Elf.
- **Implementation**: The function opens the provided file, reads its contents, and processes the data. It splits the input into separate inventories for each Elf and calculates the total calories for each Elf's inventory. The function then determines the maximum of these totals.

### `total_calories_top_three(file_path)`

- **Purpose**: This function, similar to the first, calculates the total calories carried by the top three Elves with the most calories in their food supply.
- **Implementation**: It follows a similar approach to reading and processing the file. However, instead of finding the maximum, it sorts all the total calorie counts in descending order and sums up the top three values.

## Usage

1. **Prepare the Data File**: Ensure you have a text file (`elfcals.txt`) with the calorie data. Each Elf's food items should be listed one per line with the calorie count, and each Elf's inventory should be separated by a blank line.

2. **Run the Functions**:
    - To find the Elf with the maximum calorie count:
      ```python
      print("Max calories by a single Elf:", max_calories_from_file('elfcals.txt'))
      ```

    - To find the total calories of the top three Elves:
      ```python
      print("Total calories by top three Elves:", total_calories_top_three('elfcals.txt'))
      ```

## Requirements

- Python 3.x

## License

Copyright (c) 2023 Kayden Cormier
Copyright (c) 2023 K-GamesMedia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

