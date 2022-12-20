#  You need to install dependent module: FastAPI, uvicorn, tkineter
#
#       $: pip install fastapi uvicorn
#       $: sudo apt-get install python3.10-tk
#
#  Then, run this script:     
#       
#       $: uvicorn main:app --reload



from fastapi import FastAPI, Request
import uvicorn
import json
# 引入訊息視窗模組
import tkinter as tk
import tkinter.messagebox

app = FastAPI()

msg = ""

# Server

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/behavior")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['broom'], data['motion'], data['mop'])
    if data['light'] == "false" and int(data['weight']) > 5: # light off and on the bed
        print("Sleeping")
        msg = "He is sleeping."
    elif data['light'] == "true" and int(data['weight']) > 5: # light on and on the bed
        print("Awake")
        msg = "He is awake."
    elif data['light'] == "false"  and int(data['weight']) < 5 and data['door'] == "true": # turn the light off, leave the bed, and open the door
        print("Go out")
        msg = "He is going out."
    tkinter.messagebox.showinfo(message = msg)   # 訊息內容
    return "clean suc"

@app.post("/aircon")
async def t(
    request: Request
):
    data = await request.json()
    print(data, data['temperature'], data['aircon'], type(data['aircon']))
    if data['aircon'] == "true":
        if int(data['temperature']) > 28:
            print("Cool mode")
            msg = "The temperature is: " + data['temperature'] + "\nTurn on the air conditioner\n Mode: Cool"
        elif int(data['temperature']) < 20:
            print("Heat mode")
            msg = "The temperature is: " + data['temperature'] + "\nTurn on the air conditioner\n Mode: Heat"
        else:
            print("Fan mode")
            msg = "The temperature is: " + data['temperature'] + "\nTurn on the air conditioner\n Mode: Fan"
    else:
        print("Air conditioner off")
        msg = "Air conditioner off"
    tkinter.messagebox.showinfo(message = msg)   # 訊息內容
    return "aircon suc"

@app.post("/clean")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['light'], data['weight'], data['door'])
    if data['motion'] == "false":
        print("Doing nothing")
        msg = "He is doing nothing."
    else:
        if data["broom"] == "true" and data["mop"] == "false":
            print("Act: Cleaning the room")
            print("Sub-act: Sweeping the floor")
            msg = "He is sweeping the floor."
        elif data["mop"] == "true" and data["broom"] == "false":
            print("Act: Cleaning the room")
            print("Sub-act: Mopping the floor")
            msg = "He is mopping the floor."
        else:
            print("Working but not mopping or sweeping")
            msg = "He is working but not cleaning the room."
    tkinter.messagebox.showinfo(message = msg)      # 訊息內容
    return "behavior suc"

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)