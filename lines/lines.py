import sys  # Import sys to handle command-line arguments and exit the program
import os   # Import os to check if the file exists

def main():
    # Make sure there is exactly one command-line argument and it ends with .py
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py <filename>.py")  # Exit with a usage message

    # Get the filename from the argument
    filename = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: {filename} does not exist.")  # Exit if the file doesn't exist

    loc = 0  # Line of code counter

    # Open the file and read each line
    with open(filename) as file:
        for line in file:
            stripped_line = line.strip()  # Remove spaces and tabs from the start and end
            # Count the line only if it's not empty and not a comment (starting with #)
            if stripped_line and not stripped_line.startswith("#"):
                loc += 1  # Add to the line of code counter

    # Print the total number of lines of code
    print(f"Number of lines of code: {loc}")

# Run the main function only if the file is executed directly
if __name__ == "__main__":
    main()