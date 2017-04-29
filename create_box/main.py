"""This is the entry point of the program."""


def create_box(height, width, character):
    if height <= 0 or width <= 0:
        return "Invalid Entry"
    box_string = ""
    for row in range(height):
        for column in range(width):
            box_string += character
        box_string += "\n"
    return box_string

def create_box_empty(height, width, character):
    if height <= 0 or width <= 0:
        return "Invalid Entry"
    box_string = ""
    for row in range(height):
        if row == 0 or row == height-1:
            for column in range(width):
                box_string += character

        else:
            for column in range(width):
                if column == 0 or column == width-1:
                    box_string += character
                else:
                    box_string += " "
        box_string += "\n"        
                
    return box_string


if __name__ == '__main__':
    create_box(3, 4, '*')
    