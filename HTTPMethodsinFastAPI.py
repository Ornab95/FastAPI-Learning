# from locale import str
# from rich.status import status
from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/patients/{Pid}")
def getPatiestById(Pid: str = Path(..., description="Id of the patient in string", example="P001")):
    data = viewData()
    if Pid in data:
        return data[Pid]
    raise HTTPException(status_code = 404, detail= "Patient not found." )

@app.get("/sort")
def sortPatient(sortBy: str = Query(...,description="Sort on the bases of Height, Weight,BMI"),order: str = Query("asc", description="Sort by Ascending order")):
    validField = ['height','weight','bmi']
    if sortBy not in validField:
        raise HTTPException(status_code=400,detail=f"Invalid Row Selected{validField}")

    if order not in ['asc','dsc']:
        raise HTTPException(status_code=400, detail="Invalid Order selected")
    data = viewData()
    sortOrder = True if order == 'dsc' else False
    sortedData = sorted(data.values(),key = lambda x: x.get(sortBy,0),reverse=sortOrder) 
    return sortedData