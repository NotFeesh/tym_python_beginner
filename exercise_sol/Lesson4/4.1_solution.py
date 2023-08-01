alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    

def generate_seating_chart(rows, seats_per_row):
    seating_chart = []
    # CODE
    for row in range(1, rows + 1):
        row_seats = []
        for seat in range(1, seats_per_row + 1):
            row_seats.append(f"{alphabet[row - 1]}{seat}")
        seating_chart.append(row_seats)
    # You do not have to code anything past this point
    return seating_chart
    
def display_seating_chart(seating_chart):
    print("Seating Chart:")
    print("-------------------")
    for row, seats in enumerate(seating_chart, 1):
        print(f"Row {alphabet[row - 1]}: {seats}")
    print("-------------------")

# Get user input
rows = int(input("Enter the number of rows: "))
seats_per_row = int(input("Enter the number of seats per row: "))

# Generate and display seating chart
seating_chart = generate_seating_chart(rows, seats_per_row)
display_seating_chart(seating_chart)
