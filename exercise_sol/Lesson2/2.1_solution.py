floor_max = int(input("Please enter maximum floor number:"))

print("Enter 0 to exit")
while True:
    floor_target = int(input("Please enter the number of the floor you want to go to."))
    if floor_target > floor_max or floor_target < 0:
        print("That floor doesn't exist!")
        continue
    elif floor_target == 0:
        print("Thank you for using the elevator!")
        break
    print(f"Travelling to floor {floor_target}.")