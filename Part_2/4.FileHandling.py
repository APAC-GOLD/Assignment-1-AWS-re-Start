# Write a function which reads a file name, eg. `input.txt`, then print out all the lines in the files
# Additionally, display the lines in such a way that does not cause line misalignment
# Save all the printout into a separate file called `output.txt`
#
# ```
# 1.  ASDHKJAAS
# 2.  HNHSAFKSK
# ...
# 10. ASFASKFDS
# ...
# ```
def format_text_file(input_path: str):
    # ========================================================================
    input_path: str = "/Users/gold/Projects/Assignments/Assignment1/restart-q4-2023-assignment-amy/Part_2/input.txt"
    with open(input_path, "r") as f:
        lines = f.readlines()
        with open("output.txt", "w") as out_file:
            for line in lines:
                out_file.write(line)
                print(line, end="")
    # ========================================================================
    pass


def main():
    format_text_file("input.txt")


if __name__ == "__main__":
    main()
