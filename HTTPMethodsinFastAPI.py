from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"This is a app where i learn FastAPi and try to make a CRUD app of patient managment system"}

def viewData():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data
def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

@app.get("/allPatients")
def allData():
    return viewData()

@app.post("/addPatient")    
def addPatient(patient: dict):
    data = viewData()
    data[patient["id"]] = patient
    saveData(data)
    return {"message": "Patient added successfully"}