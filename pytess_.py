# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd ='/opt/homebrew/bin/tesseract'
# # Load the image
# image = Image.open("https://i.stack.imgur.com/i1Abv.png")

# # Perform OCR
# text = pytesseract.image_to_string(image)

# # Print the extracted text
# print(text)

import requests
from PIL import Image
import pytesseract
from io import BytesIO  # Import BytesIO from the io module
pytesseract.pytesseract.tesseract_cmd ='/opt/homebrew/bin/tesseract'
# URL of the image
image_url = 'https://i.stack.imgur.com/i1Abv.png'

# Download the image from the URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))  # Use BytesIO to create a file-like object from the response content

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

