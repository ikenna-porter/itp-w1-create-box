"""This is the entry point of the program."""


def create_box(height, width, character):
    box_string = ""
    for row in range(height):
        for column in range(width):
            box_string += character
        box_string += "\n"
    return box_string


if __name__ == '__main__':
    create_box(3, 4, '*')
