def roman_to_int(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string in reverse
    for char in reversed(s):
        current_value = roman_map[char]
        
        # If the current value is less than the previous value, it means we need to subtract
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Update the previous value
        prev_value = current_value

    return total

# Test cases
print(roman_to_int("III"))        # Output: 3
print(roman_to_int("LVIII"))      # Output: 58
print(roman_to_int("MCMXCIV"))    # Output: 1994
print(roman_to_int("IX"))         # Output: 9
print(roman_to_int("XL"))         # Output: 40
print(roman_to_int("CDXC"))       # Output: 490




