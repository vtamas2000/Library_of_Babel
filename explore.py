import lib_of_babel.babel as babel
import re


def main():
    print(
        "Welcome to the Library of Babel\n"
        + "Enter either a sequence of numbers separated by '-' to view the content of the book on chamber-wall-shelf-volume\n"
        + "Or a string to get first volume that the string appears in\n\n"
        + "Chamber can be any integer, wall must be 0-3, shelf must be 0-5, volume must be 0-31\n"
    )

    while True:
        prompt = input("Enter a sequence of numbers or a string to search\n")
        prompt_re = re.match(r"^(\d+)-(\d+)-(\d+)-(\d+)$", prompt)

        if prompt == "e":
            break

        if prompt_re:
            chamber = int(prompt_re.group(1))
            wall = int(prompt_re.group(2))
            shelf = int(prompt_re.group(3))
            volume = int(prompt_re.group(4))

            if (
                wall not in [0, 1, 2, 3]
                or shelf not in [0, 1, 2, 3, 4]
                or volume not in [i for i in range(32)]
            ):
                print(
                    "Chamber can be any integer, wall must be 0-3, shelf must be 0-5, volume must be 0-31\n"
                )
                continue
            else:
                print(babel.get_text(chamber, wall, shelf, volume))
        else:
            print(babel.find_str(prompt))


if __name__ == "__main__":
    main()
