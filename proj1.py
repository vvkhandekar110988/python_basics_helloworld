weight = int(input('Weight: '))
unit = input('(L) for LBS and (K) for Kilograms')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
160