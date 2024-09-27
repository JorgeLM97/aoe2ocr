import pytesseract

# import pyautogui
from PIL import Image, ImageOps

cfg_file = "tesseract_config"


def load_image(file_path):
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        return None


# def take_screenshot():
#    return pyautogui.screenshot()


def apply_mask(image, mask_path):
    mask = load_image(mask_path)
    if mask:
        return Image.blend(image, mask, 0.5)
    else:
        print("Mask not found")
        return image


def image_processing(image):
    # Crop the image to the desired region
    image = image.crop((0, 0, 575, 50))

    # debug
    image.save("step1.jpg")

    # Invert the image colors
    image = ImageOps.invert(image)
    image.save("step2.jpg")

    # Convert the image to grayscale
    image = ImageOps.grayscale(image)
    image.save("step3.jpg")

    return image


def perform_ocr(image):
    try:
        return pytesseract.image_to_string(image, lang="eng", config="--psm 6")
    except pytesseract.TesseractError as e:
        print(f"Error during OCR: {e}")
        return ""


def main():

    # Get a saved screenshot from the disk if available
    screenshot = load_image("screenshot.jpg")

    # Take a screenshot if no image found

    # if screenshot is None:
    # print("Screenshot not found")
    # screenshot = take_screenshot()

    # Process the image
    final_image = image_processing(screenshot)

    snip1 = final_image.crop((8, 32, 48, 48))
    snip1.save("snip1.jpg")

    snip2 = final_image.crop((108, 32, 148, 48))
    snip2.save("snip2.jpg")

    snip3 = final_image.crop((208, 32, 248, 48))
    snip3.save("snip3.jpg")

    snip4 = final_image.crop((308, 32, 348, 48))
    snip4.save("snip4.jpg")

    snip5 = final_image.crop((408, 32, 448, 48))
    snip5.save("snip5.jpg")

    # Apply OCR to the image
    text1 = perform_ocr(snip1)
    text2 = perform_ocr(snip2)
    text3 = perform_ocr(snip3)
    text4 = perform_ocr(snip4)
    text5 = perform_ocr(snip5)

    # Print the detected text
    print("Wood ", text1)
    print("Food ", text2)
    print("Gold ", text3)
    print("Stone ", text4)
    print("Vills ", text5)


if __name__ == "__main__":
    main()
