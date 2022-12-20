#  You need to install dependent module: FastAPI, uvicorn
#
#       $: pip install fastapi uvicorn
#
#  Then, run this script:     
#       
#       $: uvicorn main:app --reload



from fastapi import FastAPI, Request
import uvicorn
import json

app = FastAPI()

# # Variables set up

# broom = False 	    # bool
# motion = True 	    # bool
# mop = False		    # bool

# temperature = 26 	# int
# aircon = False		# bool

# light = False		# bool
# weight = 45 	    # int
# door = False		# bool

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
    elif data['light'] == "true" and int(data['weight']) > 5: # light on and on the bed
        print("Awake")
    elif data['light'] == "false"  and int(data['weight']) < 5 and data['door'] == "true": # turn the light off, leave the bed, and open the door
        print("Go out")
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
        elif int(data['temperature']) < 20:
            print("Heat mode")
        else:
            print("Fan mode")
    else:
        print("Air conditioner off")
    return "aircon suc"

@app.post("/clean")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['light'], data['weight'], data['door'])
    if data['motion'] == "false":
        print("Doing nothing")
    else:
        if data["broom"] == "true" and data["mop"] == "false":
            print("Act: Cleaning the room")
            print("Sub-act: Sweeping the floor")
        elif data["mop"] == "true" and data["broom"] == "false":
            print("Act: Cleaning the room")
            print("Sub-act: Mopping the floor")
        else:
            print("Working but not mopping or sweeping")
    return "behavior suc"

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)