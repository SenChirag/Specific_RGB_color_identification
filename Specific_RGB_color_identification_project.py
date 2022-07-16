from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0


def main():
    print("....Welcome to this Specific RGB Color Identification program....")
    originalInput = input("Enter the location of the Image : ")
    print("Select the specific RGB color you want to identify :")
    print("1: Red")
    print("2: Green")
    print("3: Blue")

    optionSelected = int(input("-> "))
    if optionSelected == 1 or 2 or 3:
        img = SimpleImage(originalInput)
        img.show()
        edited_Image = color_input(originalInput, optionSelected)
        edited_Image.show()


def color_input(file_name, option):
    image = SimpleImage(file_name)
    for pixel in image:
        if option == 1:
            pixel.red = pixel.red - (pixel.green / 2) - (pixel.blue / 2)
            pixel.green = pixel.red
            pixel.blue = pixel.red
        elif option == 2:
            pixel.green = pixel.green - (pixel.red / 2) - (pixel.blue / 2)
            pixel.red = pixel.green
            pixel.blue = pixel.green
        elif option == 3:
            pixel.blue = pixel.blue - (pixel.red / 2) - (pixel.green / 2)
            pixel.red = pixel.blue
            pixel.green = pixel.blue
    return image


if __name__ == "__main__":
    main()