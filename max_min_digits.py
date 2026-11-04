import sys

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: python {sys.argv[0]} <integer>")

try:
    input_number = int(sys.argv[1])
except ValueError:
    raise SystemExit("Please provide a valid integer.")

temp = abs(input_number)
max_digit = min_digit = temp % 10

while temp > 0:
    remainder_digit = temp % 10
    if remainder_digit > max_digit:
        max_digit = remainder_digit
    if remainder_digit < min_digit:
        min_digit = remainder_digit
    temp //= 10

print(f"max digit is {max_digit}, min digit is {min_digit}")

