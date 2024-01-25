#1 Pyramid

i = int(input("Enter a number for pyramid: "))

print("\nNormal Pyramid")
for e in range(i):
    x = '* '
    x = x*e
    print(f"{x: ^10}")

#2 Invert Pyramid
print("\nInvert Pyramid\n")
for e in range(i):
    x='* '
    x=x*(i-e)
    print(f'{x: ^10}')

#3 Lef side pyramid
print("\nLeft sided Pyramid\n")
for e in range(i):
    x='* '
    x=x*e
    print(f'{x: <10}')

#4 Right sided pyramid
print("\nRight sided pyramid\n")
for e in range(i):
    x='* '
    x=x*e
    print(f"{x: >10}")


print(f"\n---End---")
