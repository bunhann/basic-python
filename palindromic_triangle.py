n = int(input("Enter a number (1-9):")) # Enter number n<=9
for i in range(1, n+1):
  print(((10 ** i - 1) // 9) ** 2)
