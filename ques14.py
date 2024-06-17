lines = []

print("Enter multiple lines of input. Enter an empty line to stop.")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nThe lines you entered are:")
for line in lines:
    print(line)
