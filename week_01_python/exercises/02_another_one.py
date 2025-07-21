# credits: datalemur.com

# From an integer array digits, where each digits[i] is the ith digit of positive whole number. 
# It is ordered from most significant to least significant digit.
# Return an array of digits of the number after adding another one to the input.

# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]

def another_one(digits):
    # Start from the last digit
    i = len(digits) - 1
    while i >= 0 and digits[i] == 9:
        # Change all 9s to 0
        digits[i] = 0
        i -= 1

    # If we found a non-9 digit, just add 1
    if i >= 0:
        digits[i] += 1
        return digits
    else:
        # All digits were 9, so add a leading 1
        return [1] + digits