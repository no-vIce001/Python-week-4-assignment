#Program that reads a file specified by the user, modifies its content, and writes the modified content to a new file. It also handles potential file not found and read errors.
def modify_file():

    try:
        input_filename = input("Enter the name of the file to read: ")
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        output_filename = f"modified_{input_filename}"
        with open(output_filename, 'w') as outfile:
            for line in content:
                # Modify the line here (example: convert to uppercase)
                modified_line = line.lower()
                outfile.write(modified_line)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file.")

if __name__ == "__main__":
    modify_file()