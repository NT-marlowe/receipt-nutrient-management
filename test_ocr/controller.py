import base64
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
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
import uvicorn

from google.cloud import vision


app = FastAPI()
client = vision.ImageAnnotatorClient()
origins = [
    "http://localhost",
    "http://localhost:8080",
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost:3000/new-image',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


file_name = os.path.abspath('./sample.jpg')


#app.mount("/static", StaticFiles(directory="static"), name="static")

class Body(BaseModel):
    date: str
    base64Txt: str
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

    return JSONResponse(content=n_dict)

if __name__ == "__main__":
    uvicorn.run(app)