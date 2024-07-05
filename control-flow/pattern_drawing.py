pattern_size = int(input("Enter the size of the pattern"))
count = pattern_size

while count != 0:
    count = count - 1
    for i in range(pattern_size):
        print("*", end="")
    print()

#count variable 
# if count 