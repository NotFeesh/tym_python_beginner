stations = ["Punggol", "Sengkang", "Buangkok", "Hougang", "Kovan", "Serangoon"]

print("Hi! My name is Albert!")

for station in stations:
    if station == "Kovan":
        break
    print(f"I just passed {station}!")

print(f"I finally arrived at {station}!")