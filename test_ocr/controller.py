import base64
from cv2 import AgastFeatureDetector
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
from starlette.responses import RedirectResponse
from culc import culculation
import uvicorn
import db
from  models import Receipt
from datetime import datetime
from google.cloud import vision


app = FastAPI()
client = vision.ImageAnnotatorClient()
# front側とback側のoriginを両方書く必要があるのかな？
origins = [
    "http://localhost",
    "http://localhost:8080",
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost:3000/summary',
    'http://localhost:3000/new-image',
    'http://localhost:3000/history',
    'http://localhost:8000/uploadimg',
    'http://localhost:8000/summary',
    'http://localhost:8000/history',
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
    n_list = culculation(output_text)
    date = datetime.strptime(body.date, '%Y-%m-%d')
    protein = n_list[0]
    carbon = n_list[1]
    fat = n_list[2]
    mineral = n_list[3]
    vitamin = n_list[4]
    fiber = n_list[5]
    description = body.description
    
    receipt = Receipt(date, protein, carbon, fat, mineral, vitamin, fiber, description)
    db.session.add(receipt)
    db.session.commit()
    db.session.close()
    n_dict = {
        'protein':protein,
        'carbon':carbon,
        'fat':fat,
        'mineral':mineral,
        'vitamin':vitamin,
        'fibar':vitamin
        }
    return JSONResponse(n_dict)




@app.get('/summary/')
def viewsummery():
    receipt = db.session.query(Receipt).all()
    db.session.close()
    protein_score = 0
    carbon_score = 0
    fat_score = 0
    mineral_score = 0
    vitamin_score = 0
    fiber_score = 0
    count = 0
    for r in receipt:
        protein_score += r.protein
        carbon_score += r.carbon
        fat_score += r.fat
        mineral_score += r.mineral
        vitamin_score += r.vitamin
        fiber_score += r.fiber
        count += 1
        print(r.mineral)

    mag = 20
    summary = {
        'protein':mag * protein_score/count,
        'carbon':mag * carbon_score/count,
        'fat':mag * fat_score/count,
        'mineral':mag * mineral_score/count,
        'vitamin':mag * vitamin_score/count,
        'fiber':mag * fiber_score/count,
    }
    return JSONResponse(summary)

@app.get('/history/')
def viewhistory():
    receipt = db.session.query(Receipt).all()
    db.session.close()
    mag = 20
    hist_dict = []
    for r in receipt:
        l = {
            "ID":r.id,
            "date": str(r.date),       
            "protein":r.protein * mag,
            "carbon":r.carbon * mag,
            "fat":r.fat * mag,
            "vitamin":r.vitamin * mag,
            "mineral": r.mineral * mag,    
            "fiber":r.fiber * mag,
            "description": r.description
        }
        
        hist_dict.append(l)
    
    
    # return JSONResponse(hist_dict)
    return hist_dict



if __name__ == "__main__":
    uvicorn.run(app)
