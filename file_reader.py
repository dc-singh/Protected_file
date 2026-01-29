try:
    usr_input = input("Enter the file name: ")

    if usr_input.strip() == '':
        print("You didn't enter the file name")
        exit()

    with open(usr_input, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check filename")

except PermissionError:
    print("You do not have permission to read this file")

finally:
    print("Operation Finished")