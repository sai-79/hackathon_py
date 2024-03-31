import boto3

# Initialize the Textract client
textract_client = boto3.client('textract', region_name='us-east-1')
pytesseract.pytesseract.tesseract_cmd ='/opt/homebrew/bin/pytesseract'

# Read the image file as bytes
with open('image.jpeg', 'rb') as image_file:
    image_bytes = image_file.read()

# Call Textract to analyze the image and extract text
response = textract_client.detect_document_text(
    Document={
        'Bytes': image_bytes
    }
)

# Extract text from the response
extracted_text = ""

for item in response['Blocks']:
    if item['BlockType'] == 'LINE':
        extracted_text += item['Text'] + "\n"

# Print the extracted text
print(extracted_text)
