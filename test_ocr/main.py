from http import client
import io
import os
from urllib import response

from culc import culculation

from google.cloud import vision

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('./sample2.png')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.document_text_detection(
    image=image,
)

output_text = ''
for page in response.full_text_annotation.pages:
    for block in page.blocks:
        for paragraph in block.paragraphs:
            for word in paragraph.words:
                output_text += ''.join([
                    symbol.text for symbol in word.symbols
                ])

print(output_text)

print(culculation(output_text))