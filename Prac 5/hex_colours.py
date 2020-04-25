COLOUR_TO_CODE = {"black": "#000000",
                  "blue": "#0000ff",
                  "brown": "#a5522a",
                  "white": "#ffffff",
                  "green": "#00ff00",
                  "yellow": "#ffff00",
                  "red": "#ff0000",
                  "purple": "#9b30ff",
                  "pink": "#ffc0cb",
                  "orange": "#ffa500"}


def main():
    colour = input("Enter the colour :").lower()
    while colour != "":
        print("Colour code for {} is {}".format(colour, COLOUR_TO_CODE.get(colour)))
        colour = input("Enter the colour :")


if __name__ == '__main__':
    main()
