def main():
    path = input("Please enter the filepath: ")
    try:
        with open(path, "r") as file:
            lines = file.readlines()

        # Sort the lines
        lines.sort()

        with open(path, "w") as file:
            file.writelines(lines)

    except FileNotFoundError:  # Be specific about the exception
        print("Invalid file path")

if __name__ == "__main__":
    main()

