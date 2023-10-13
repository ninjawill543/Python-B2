#f-string (formatted strings)

date = "11/06/2004"

uno=date[0:2]

dos=date[3:5]

tres=date[6:]

print(f"{uno}.{dos}.{tres}")

habitants = 7_753_000_000
superficie = 149_000_000

print(f"nb habitant par km2: {round(habitants/superficie, 2)}")