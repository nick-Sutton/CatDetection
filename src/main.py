from cam import cam
from image import testImages
from consoleheader import logo_format, info_layout

def main():
    logo_format()
    info_layout()

    while True:
        try:
            viewer = int(input("What would you like to do: \n(1)input an image: \n(2)activate a camera: \n"))
            if viewer == 1:
                print("Loading...")
                testImages()
            elif viewer == 2:
                print("Loading...")
                cam()
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            break
    
if __name__ == '__main__':
    main()