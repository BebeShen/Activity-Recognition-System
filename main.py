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


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/test")
async def t(
    request: Request
):
    data = await request.json()
    print(data, data['state'])
    return "suc"

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)