import base64
from django.http import JsonResponse
from fastapi import FastAPI, File, UploadFile
import json
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import numpy as np
import cv2
from http import client
import io
import os
from urllib import response
from fastapi.responses import JSONResponse
from culc import culculation

from google.cloud import vision


app = FastAPI()
client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('./sample.jpg')


app.mount("/static", StaticFiles(directory="static"), name="static")

class Body(BaseModel):
    base64Txt: str
    date: int
    description: str

@app.post('/uploadimg/')
def receiveimg(body: Body):
    imgjson = body.base64Txt

    img_binary = base64.b64decode(imgjson.encode())
    jpg = np.frombuffer(img_binary,dtype=np.uint8)
    img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
    cv2.imwrite(file_name,img)
    
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
    os.remove("./sample.jpg")
    n_dict = culculation(output_text)

    return JsonResponse(n_dict)