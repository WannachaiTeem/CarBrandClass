from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
# from app.code import predictModel
import pickle
import os


# สำหรับเรียกใช้แบบ Docker
rd = pickle.load(open(os.getcwd()+r'/model/ClassifierCarModel.pkl','rb'))

# สำหรับเรียกใช้แบบ Localhost
# rd = pickle.load(open(r'..\model\ClassifierCarModel.pkl','rb'))

def predictModel(hogread):
    mb = rd.predict(hogread)
    return mb[0]


# อนุญาตให้ทุกโดเมน (origin) สามารถทำคำขอเข้าสู่ api นี้ได้
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  
    allow_methods=['*'],  
    allow_headers=['*']   
)

@app.get("/")
def read_root():
    return {"Brand Car is"}

# api สำหรับ Predict
@app.post("/api/carbrand") 
async def read_image(request: Request): 
                        # localhost:8080 172.17.0.2
    path_gethog = 'http://172.17.0.2:80/api/gethog/'
    data = await request.json()
    hogread = requests.post(path_gethog, json=data)
    hogread = hogread.json()['HOG']
    hogread =  predictModel([hogread])
    return {"to is Brand" : hogread}