import pytesseract
import pyautogui
from PIL import Image, ImageOps


def load_image(file_path):
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        return None


def take_screenshot():
    return pyautogui.screenshot()


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

    #Invert the image colors
    image = ImageOps.invert(image)
    image.save("step2.jpg")

    # Convert the image to grayscale
    image = ImageOps.grayscale(image)
    image.save("step3.jpg")

    return image

def perform_ocr(image):
    try:
        return pytesseract.image_to_string(image)
    except pytesseract.TesseractError as e:
        print(f"Error during OCR: {e}")
        return ""


def main():

    # Get a saved screenshot from the disk if available
    screenshot = load_image("screenshot.jpg")
    
    # Take a screenshot if no image found
    if screenshot == None:
        screenshot = take_screenshot()

    # Process the image
    final_image = image_processing(screenshot)

    # Apply OCR to the image
    text = perform_ocr(final_image)

    # Print the detected text
    print(text)


if __name__ == "__main__":
    main()