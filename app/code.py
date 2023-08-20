import pickle
import os 
import json

# สำหรับเรียกใช้แบบ Docker
rd = pickle.load(open(os.getcwd()+r'/model/ClassifierCarModel.pkl','rb'))

# สำหรับเรียกใช้แบบ Localhost
# rd = pickle.load(open(r'..\model\ClassifierCarModel.pkl','rb'))

def predictModel(hogread):
    mb = rd.predict(hogread)
    return mb[0]

# #การอ่านไฟล์dataHOG.json
# with open(r'app\dataHOG.json','r') as dh :
#     data = json.load(dh)["HOG"]
# print("Data :",predictModel([data]))