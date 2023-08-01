alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    

def generate_seating_chart(rows, seats):
    # You may not understand this part, but rows is the number of rows we need to create, with seats being the number of seats in each row
    seating_chart = []
    # CODE
    for row in range(rows):
        row_seats = []
        for seat in range(1, seats + 1):
            row_seats.append(f"{alphabet[row]}{seat}")
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
seats = int(input("Enter the number of seats per row: "))

# Generate and display seating chart
seating_chart = generate_seating_chart(rows, seats)
display_seating_chart(seating_chart)
