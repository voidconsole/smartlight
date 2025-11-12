import serial
import pyautogui
import numpy as np
from PIL import Image

# Initialize serial communication with Arduino
ser = serial.Serial('COM4', 9600) 

def find_average_color():
    # Capture screenshot and convert to RGB mode
    screenshot = pyautogui.screenshot()
    img = Image.new("RGB", screenshot.size)
    img.paste(screenshot)
    # Resize image for faster processing
    img = img.resize((100, 100))
    # Convert image to numpy array
    img_array = np.array(img)
    # Calculate average color
    avg_color = tuple(np.average(img_array, axis=(0, 1)).astype(int))
    return avg_color

def send_color_to_arduino(color):
    # Extract RGB components
    r, g, b = color
    # Write color data to Arduino
    ser.write(bytes([r, g, b]))

while True:
    average_color = find_average_color()
    send_color_to_arduino(average_color)
