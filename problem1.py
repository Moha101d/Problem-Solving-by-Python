height = int(input("Enter height: "))

for i in range(height):
    row = []

    # Make the left side: 2^0 to 2^i
    for j in range(i + 1):
        row.append(2 ** j)

    # Make the right side: 2^(i-1) to 2^0
    for j in range(i - 1, -1, -1):
        row.append(2 ** j)

    # Convert all numbers to strings
    row_str = [str(x) for x in row]

    # Join with space
    line = " ".join(row_str)

    # Print with spaces in front to center it
    spaces = " " * (height - i) * 2
    print(spaces + line)