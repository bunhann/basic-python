smallest = None
print("Before: ", smallest)
for i in [3, 42, 21, 23,5]:
    if smallest is None or i < smallest:
        smallest = i
        break
    print("Loop: ", i, smallest)
print("Smallest Number: ", smallest)