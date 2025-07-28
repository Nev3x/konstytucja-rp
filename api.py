import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/konstytucja/{artykul}")
async def konstytucja(artykul:int):
    text_file = f"C:\\Users\\{os.environ.get('username')}\\Desktop\\w\\konstytucjarp\\konstytucja\\konstytucja_art{artykul}.txt"
    with open(text_file, 'r') as file:
        full_art = ''
        lines = file.readlines()
        for line in lines:
            full_art += line

        return full_art
if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, host="127.0.0.1")