number = int(input("Enter a number to see its multiplication table:"))

for no in range(1,11):
    result = number*no
    print(number, "*", no, "=", result)
