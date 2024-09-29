import sys

valid_cs = []

def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    if command not in valid_cs:
        print(f"{command}: command not found")
    main()

if __name__ == "__main__":
    main()
