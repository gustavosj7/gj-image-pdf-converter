from PIL import Image

try:
    # Ask the user for the filename
    filename = input("Type the name of your image: ")

    # Add extension if missing
    if not filename.endswith(".jpg"):
        filename = filename + ".jpg"

    # Open the image
    image = Image.open(filename)

    # Convert the image to RGB (required for PDF)
    converted_image = image.convert("RGB")

    # Generate new name and save
    new_name = filename.replace(".jpg", ".pdf")
    converted_image.save(new_name)

    print("Image converted to PDF successfully!")

except FileNotFoundError:
    print("File not found, please select a valid file!")
