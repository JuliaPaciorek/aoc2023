# %%
'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
'''
#get each line
# get first and last digit of each line
# combine 1,2 =  12
# %%
from pathlib import Path
# part 1
calibration = 0
input_file = 'C:/Users/julia/repos/aoc/input.txt'
for line in Path(input_file).read_text().splitlines():
    numbers = [char for char in line if char.isdigit()]
    calibration += int(numbers[0] + numbers[-1])

# %%
'''
Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with thiss new information, you now need to find the real first and last digit on each line. For example:
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",    
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
# %%
#part 2
def check_front(line):
    word = ""
    for char in line:
        if char.isdigit():
            return char
        word += char
        if len(word) >= 3:
            for key in numbers:
                if key in word:
                    return numbers[key]

def check_back(line):
    word = ""
    for char in reversed(line):
        if char.isdigit():
            return char
        word = list(word)
        word.insert(0, char)
        word = ''.join(word)
        if len(word) >= 3:
            for key in numbers:
                if key in word:
                    return numbers[key]
# %%
input_file = 'C:/Users/julia/repos/aoc/input.txt'
calibration = 0
for line in Path(input_file).read_text().splitlines():
    calibration += int(check_front(line) + check_back(line))

calibration
