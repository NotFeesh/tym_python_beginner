alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    

def generate_seating_chart(rows, seats):
    seating_chart = []
    # CODE 
    
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
