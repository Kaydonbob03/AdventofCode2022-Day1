const fs = require('fs');

function maxCaloriesFromFile(filePath) {
    const input_data = fs.readFileSync(filePath, 'utf8');

    // Split the data into separate inventories for each Elf
    const elfInventories = input_data.trim().split('\n\n');

    // Initialize a variable to keep track of the maximum calories
    let maxCalories = 0;

    for (const elf of elfInventories) {
        // Calculate the total calories for each Elf
        // Sum up the calorie values, converting each line to an integer
        const calories = elf.split('\n')
            .filter(line => /^\d+$/.test(line)) // Filter lines with digits only
            .map(line => parseInt(line))
            .reduce((sum, value) => sum + value, 0);

        // Update maxCalories if this Elf's total is greater
        maxCalories = Math.max(maxCalories, calories);
    }

    return maxCalories;
}

function totalCaloriesTopThree(filePath) {
    const input_data = fs.readFileSync(filePath, 'utf8');

    const elfInventories = input_data.trim().split('\n\n');

    // Array to store the total calories for each Elf
    const allCalories = [];

    for (const elf of elfInventories) {
        const calories = elf.split('\n')
            .filter(line => /^\d+$/.test(line)) // Filter lines with digits only
            .map(line => parseInt(line))
            .reduce((sum, value) => sum + value, 0);

        // Append the total calories of this Elf to the array
        allCalories.push(calories);
    }

    // Calculate the sum of the top three highest calorie counts
    const totalTopThree = allCalories.sort((a, b) => b - a).slice(0, 3).reduce((sum, value) => sum + value, 0);

    return totalTopThree;
}

// File containing the Elves' calorie data
const filePath = 'elfcals.txt';

console.log("Max calories by a single Elf:", maxCaloriesFromFile(filePath));
console.log("Total calories by top three Elves:", totalCaloriesTopThree(filePath));
