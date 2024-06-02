import easyocr
from PIL import ImageGrab
import pyautogui
import time

def find_text_coordinates(text):
    # Capture the screen
    screenshot = ImageGrab.grab()

    # Save the screenshot to a file
    screenshot.save('screenshot.png')

    # Create an EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the screenshot
    results = reader.readtext('screenshot.png')

    # List to store coordinates of all occurrences of the text
    coordinates_list = []

    # Loop through the OCR results and find the coordinates of the specified text
    for (bbox, word, confidence) in results:
        if word.lower() == text.lower():
            # bbox contains the coordinates of the bounding box
            (top_left, top_right, bottom_right, bottom_left) = bbox
            coordinates_list.append(bbox)

    return coordinates_list

# Find all coordinates of the string 'next' on the screen
coordinates_list = find_text_coordinates('next')

if coordinates_list:
    for coordinates in coordinates_list:
        # Calculate the center of the bounding box
        (top_left, top_right, bottom_right, bottom_left) = coordinates
        center_x = int((top_left[0] + bottom_right[0]) / 2)
        center_y = int((top_left[1] + bottom_right[1]) / 2)

        # Move the mouse to the center of the bounding box
        pyautogui.moveTo(center_x, center_y, duration=1)
        time.sleep(1)  # 1-second delay between moves

    print(f"'next' found at coordinates: {coordinates_list}")
else:
    print("'next' not found on the screen")
    