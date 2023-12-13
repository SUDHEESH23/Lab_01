def create_star_pattern(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
# Number of rows in the pattern
num_rows = 5

create_star_pattern(num_rows)
