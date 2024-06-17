try:
    with open("input.txt", "r") as file:
        content = file.read()
        print("The content of the file is:\n")
        print(content)
except FileNotFoundError:
    print("The file 'input.txt' was not found.")
