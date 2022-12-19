#  You need to install dependent module: FastAPI, uvicorn
#
#       $: pip install fastapi uvicorn
#
#  Then, run this script:     
#       
#       $: uvicorn main:app --reload



from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Variables set up

broom = False 	    # bool
motion = True 	    # bool
mop = False		    # bool

temperature = 26 	# int
aircon = False		# bool

light = False		# bool
weight = 45 	    # int
door = False		# bool

# Server

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/clean")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['broom'], data['motion'], data['mop'])
    if not light and weight > 5: # light off and on the bed
        print("Sleeping")
    elif light and weight > 5: # light on and on the bed
        print("Awake")
    elif not light and weight < 5 and door: # turn the light off, leave the bed, and open the door
        print("Go out")
    return "clean suc"

@app.post("/aircon")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['temperature'], data['aircon'])
    if aircon:
        if temp > 28:
            print("Cool mode")
        elif temp < 20:
            print("Heat mode")
        else:
            print("Fan mode")
    else:
        print("Air conditioner off")
    return "aircon suc"

@app.post("/behavior")
async def t(
    request: Request
):
    data = await request.json()
    # print(data, data['light'], data['weight'], data['door'])
    if not motion:
        print("Doing nothing")
    else:
        if broom and not mop:
            print("Act: Cleaning the room")
            print("Sub-act: Sweeping the floor")
        elif mop and not broom:
            print("Act: Cleaning the room")
            print("Sub-act: Mopping the floor")
        else:
            print("Working but not mopping or sweeping")
    return "behavior suc"

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)